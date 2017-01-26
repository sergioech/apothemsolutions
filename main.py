#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
import webapp2, jinja2, os, csv, re, random, string, hashlib, json, logging, math 

from datetime import datetime, timedelta, time
from google.appengine.ext import ndb
from google.appengine.api import mail

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.ext import deferred
from google.appengine.runtime import DeadlineExceededError

# from google.appengine.api import urlfetch
# urlfetch.set_default_fetch_deadline(900)

from python_files import datastore, constants, diccionarios_CNBV
constants = constants.constants
diccionarios_CNBV = diccionarios_CNBV.diccionarios_CNBV

DatoCNBV = datastore.DatoCNBV
CsvCNBV = datastore.CsvCNBV
TablaCNBV = datastore.TablaCNBV


template_dir = os.path.join(os.path.dirname(__file__), 'html_files')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	
	def render_html(self, template, **kw):
		t = jinja_env.get_template(template)
		return t.render(**kw)

	def print_html(self, template, **kw):
		self.write(self.render_html(template, **kw))


class Home(Handler):

	def get(self):
		self.print_html('Home.html', message = 'Hello World!')


class ChartViewer(Handler):
	def get(self):		
		self.print_html('ChartViewer.html')

	def post(self):
		chart_details = json.loads(self.request.body)

		tipo_valor = chart_details['tipo_valor']

		dl_dato = diccionarios_CNBV['des_040_11l_R0']['tipo_valor'][tipo_valor]
		desc_tec = diccionarios_CNBV['des_040_11l_R0']['tec']

		datos_cnbv = DatoCNBV.query().filter(DatoCNBV.periodo == 201611, DatoCNBV.institucion == '5', DatoCNBV.tipo_valor == tipo_valor).fetch()
		rows = []
		for dp in datos_cnbv:
			rows.append([desc_tec[dp.tec], dp.valor])

		chartData = {
			'columns' : [['string', 'Tamano empresa'],['number', dl_dato]],
			'rows' : rows,
			'title': 'Distribucion de ' + dl_dato
		}
		# print chartData

		self.response.out.write(json.dumps({
			'chartData':chartData
		}))


class NewTable(Handler):
	def get(self):
		self.print_html('NewTable.html')

	def post(self):
		post_details = get_post_details(self)

		new_table = TablaCNBV(
			nombre = post_details['nombre'],
			descripcion = post_details['descripcion'],
			url_fuente = post_details['url_fuente'])
		
		new_table.put()
		self.redirect('/TableViewer')


class TableViewer(Handler):
	def get(self):
		tablas_cnbv = TablaCNBV.query().fetch()
		upload_url = blobstore.create_upload_url('/upload_csv')
		blob_file_input = "{0}".format(upload_url)
		self.print_html('TableViewer.html', tablas_cnbv=tablas_cnbv, blob_file_input=blob_file_input)



class LoadCSV(Handler):
	def get(self):
		tabla_id = self.request.get('tabla_id')
		csv_id = self.request.get('csv_id')
		load_cnbv_csv(tabla_id, csv_id, start_key=None)
		self.redirect('/')



class CsvUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		upload = self.get_uploads()[0]
		tabla_id = self.request.get('id_tabla')
		tabla_cnbv = TablaCNBV.get_by_id(int(tabla_id))

		csv_file = CsvCNBV(
			blob_key=upload.key(),
			Key_TablaCNBV = tabla_cnbv.key,
			nombre=upload.filename,
			nombre_tablaCNBV=tabla_cnbv.nombre)
		csv_file.put()		

		self.redirect('/LoadCSV?tabla_id=' + tabla_id + '&csv_id=' + str(csv_file.key.id()))



#--- Funciones ---
def load_cnbv_csv(tabla_id, csv_id, start_key=None):

	tabla_cnbv = TablaCNBV.get_by_id(int(tabla_id))
	csv_cnbv = CsvCNBV.get_by_id(int(csv_id))

	key_tabla = tabla_cnbv.key
	key_csv = csv_cnbv.key

	blob_key = csv_cnbv.blob_key

	blob_reader = blobstore.BlobReader(blob_key)
	csv_f = csv.reader(blob_reader, dialect=csv.excel_tab)
	original_attributes = csv_f.next()[0].decode('utf-8-sig').split(',') #.decode('utf-8-sig').

	attr_dic_cnbv = diccionarios_CNBV[str('attr_' + tabla_cnbv.nombre)]

	
	# print
	# print 'Estos son los attributos originales'
	# print original_attributes 
	# print

	attributes = []

	for a in original_attributes:
		attributes.append(attr_dic_cnbv[a])

	# print
	# print 'Estos son los attributos ajustados'
	# print attributes
	# print
	# print 'Rows read when starting'
	# print start_key


	if start_key:
		for i in range(0, start_key):
			csv_f.next()
	else:
		start_key = 0

	try:
		rows_read = 0
		for row in csv_f:
			i = 0
			new_dp = DatoCNBV(tabla=key_tabla, archivo_fuente=key_csv)
			raw_dp = row[0].split(',')
			for a_key in attributes:
				a_val = raw_dp[i]

				if a_key in ['institucion', 'tec', 'estado', 'tipo_valor']:
					setattr(new_dp, a_key, (a_val.decode('utf-8')).encode('utf-8'))
				elif a_key in ['valor', 'saldo_total', 'creditos', 'acreditados']:
					setattr(new_dp, a_key, float(a_val))		
				elif a_key in ['periodo']:
					setattr(new_dp, a_key, int(a_val))

				
				i += 1							
			new_dp.put()
			rows_read += 1
			
			# print 'Rows read...'
			# print rows_read
			# print
			# print row
			# print new_dp
			# print

			# if rows_read % 10 == 0:
			# 	raise DeadlineExceededError

	except DeadlineExceededError:
		# print 'Ya fue el DeadLineExceededError'
		
		tabla_cnbv.registros += rows_read
		csv_cnbv.rows_transfered += rows_read
		tabla_cnbv.put()
		csv_cnbv.put()

		# print
		# print "Con este valor entra rows read a la excepcion"
		# print rows_read
		# print

		deferred.defer(load_cnbv_csv, blob_key, start_key + rows_read)
		return

	tabla_cnbv.registros += rows_read
	csv_cnbv.rows_transfered += rows_read
	tabla_cnbv.put()
	csv_cnbv.put()

	return


def get_post_details(self):
	post_details = {}
	arguments = self.request.arguments()
	for argument in arguments:
		post_details[str(argument)] = self.request.get(str(argument))
	return adjust_post_details(post_details)


def adjust_post_details(post_details): 
	details = {}
	for (attribute, value) in post_details.items():
		if value and value!='' and value!='None':
			details[attribute] = value
	return details



app = webapp2.WSGIApplication([
    ('/', ChartViewer),
    ('/CNBVQueries',ChartViewer),
    
    ('/NewTable', NewTable),
    ('/TableViewer', TableViewer),
    ('/LoadCSV', LoadCSV),
    ('/upload_csv', CsvUploadHandler)
], debug=True)


