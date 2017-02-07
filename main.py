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
		opciones_validas = diccionarios_CNBV.opciones_iniciales
		variables = opciones_validas['variables']
		cortes = opciones_validas['cortes'] 
		opciones = diccionarios_CNBV.opciones
		print
		print opciones
		self.print_html('ChartViewer.html', variables=variables, cortes=cortes, opciones=opciones)

	def post(self):
		chart_details = json.loads(self.request.body)

		variable = chart_details['variable']
		corte_renglones = chart_details['renglones']
		
		corte_columnas = chart_details['columnas']
		if corte_columnas == 'None':
			corte_columnas = None
		
		indice_tablas = diccionarios_CNBV.indice_inicial

		nombre_tabla = self.seleccionar_tabla(variable, corte_renglones, corte_columnas, indice_tablas)

		key_tabla = TablaCNBV.query(TablaCNBV.nombre == nombre_tabla).get().key
		datos_cnbv = DatoCNBV.query(DatoCNBV.tabla == key_tabla)		
		
		nombre_variable = variable
		tipo_variable = diccionarios_CNBV.detalles_tabla[nombre_tabla]['tipo_variables']		
		
		if tipo_variable == 'indirectas':
			variable = diccionarios_CNBV.cat_invertida_variables[variable]
			datos_cnbv = datos_cnbv.filter(DatoCNBV.tipo_valor == variable)
			variable = 'valor'

		datos_cnbv = datos_cnbv.fetch()
		chart_array = self.query_to_chart_array(datos_cnbv, variable, corte_renglones, corte_columnas, nombre_variable)

		self.response.out.write(json.dumps({
			'chart_array': chart_array,
			'title': 'Echeverria es puto'
			}))

	def seleccionar_tabla(self, variable, corte_renglones, corte_columnas, indice_tablas):
		
		if corte_columnas:
			for tabla in indice_tablas:
				variables_validas = tabla[1]
				cortes_validos = tabla[2]
				if variable in variables_validas and corte_renglones in cortes_validos and corte_columnas in cortes_validos:
					return tabla[0]
		else:
			for tabla in indice_tablas:
				variables_validas = tabla[1]
				cortes_validos = tabla[2]
				if variable in variables_validas and corte_renglones in cortes_validos:
					return tabla[0]
		return None


	def options_to_chart_array(self, rows_options, column_options, rows_title,  variable_name):
		
		array_headings = [rows_title]
		columns_position = {}
		rows_position = {}

		if column_options:
			col = 1
			for column in column_options:
				array_headings.append(column[0])
				columns_position[column[0]] = col
				col += 1
		else:
			array_headings.append(variable_name)

		numero_columnas = len(array_headings)
		chart_array = [array_headings]

		reng = 1
		for row in rows_options:
			new_row = [row[0]]
			rows_position[row[0]] = reng
			reng += 1
			for i in range(1, numero_columnas):
				new_row.append(0)
			chart_array.append(new_row)	

		return chart_array, rows_position, columns_position



	def pimp_chart_array(self, chart_array,rows_definitions, col_definitions):
		pimped_array = []

		pimped_headings = [chart_array[0][0]]

		if col_definitions:
			for heading in chart_array[0][1:]:
				pimped_headings.append(col_definitions[heading])
		else:
			pimped_headings.append(chart_array[0][1])

		pimped_array.append(pimped_headings)

		for row in chart_array[1:]:
			pimped_row = [rows_definitions[row[0]]] + row[1:]
			pimped_array.append(pimped_row)

		return pimped_array


	def query_to_chart_array(self, query_result, variable, corte_renglones, corte_columnas, nombre_variable):

		opciones = diccionarios_CNBV.opciones
		definiciones =  diccionarios_CNBV.definiciones

		row_options = opciones[corte_renglones]
		row_definitions = definiciones[corte_renglones]
		
		column_options = None
		column_definitions = None

		if corte_columnas:
			column_options = opciones[corte_columnas]
			column_definitions = definiciones[corte_columnas]
		

		chart_array, rows_position, columns_position = self.options_to_chart_array(row_options, column_options, definiciones['cortes'][corte_renglones], definiciones['variables'][nombre_variable])

		if corte_columnas:
			for dp in query_result:
				chart_array[rows_position[getattr(dp, corte_renglones)]][columns_position[getattr(dp, corte_columnas)]] += getattr(dp, variable) 
		else:
			for dp in query_result:		
				chart_array[rows_position[getattr(dp, corte_renglones)]][1] += getattr(dp, variable) 

		chart_array = self.pimp_chart_array(chart_array, row_definitions, column_definitions)	

		return chart_array


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

	tm = diccionarios_CNBV.transformation_maps_CNBV[tabla_cnbv.nombre]
	
	attributes = []
	values_map = {}

	for a in original_attributes:
		attr_map = tm[a]
		attributes.append(attr_map[0])
		if len(attr_map) == 2:
			values_map[attr_map[0]] = attr_map[1]


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
					# setattr(new_dp, a_key, (a_val.decode('utf-8')).encode('utf-8'))
					setattr(new_dp, a_key, values_map[a_key][a_val.decode('utf-8')][1])					
				elif a_key in ['valor', 'saldo_total', 'creditos', 'acreditados']:
					setattr(new_dp, a_key, float(a_val))		
				elif a_key in ['periodo']:
					setattr(new_dp, a_key, int(a_val))
				
				i += 1							
			new_dp.put()
			rows_read += 1
			
	except DeadlineExceededError:		
		tabla_cnbv.registros += rows_read
		csv_cnbv.rows_transfered += rows_read
		tabla_cnbv.put()
		csv_cnbv.put()
		deferred.defer(load_cnbv_csv, tabla_id, csv_id, start_key + rows_read)
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


