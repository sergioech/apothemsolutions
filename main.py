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

from python_files import datastore, constants
constants = constants.constants

DatoCNBV = datastore.DatoCNBV
CsvFile = datastore.CsvFile


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


class CNBVQueries(Handler):
	def post(self):
		chart_details = json.loads(self.request.body)
		cve_dato = chart_details['cve_dato']
		dl_dato = constants['cve_dl_dato'][cve_dato]

		datos_cnbv = DatoCNBV.query().filter(DatoCNBV.cve_periodo == 201611, DatoCNBV.cve_institucion == 5, DatoCNBV.cve_dato == int(cve_dato)).fetch()
		rows = []
		for dp in datos_cnbv:
			rows.append([dp.dl_TEC, dp.saldo])

		chartData = {
			'columns' : [['string', 'Tamano empresa'],['number', dl_dato]],
			'rows' : rows,
			'title': 'Distribucion de ' + dl_dato
		}
		print chartData

		self.response.out.write(json.dumps({
			'chartData':chartData
		}))



class LoadCSV(Handler):
	def get(self):
		blob_key = self.request.get('blob_key')
		load_cnbv_csv(blob_key)
		self.redirect('/')


def load_cnbv_csv(blob_key, start_key=None):
	blob_reader = blobstore.BlobReader(blob_key)
	csv_f = csv.reader(blob_reader, dialect=csv.excel_tab)
	attributes = csv_f.next()[0].decode('utf-8-sig').split(',') #.decode('utf-8-sig').
	print
	print 'Estos son los attributos'
	print attributes
	print
	
	logging.warning('Rows read when starting')
	logging.warning(start_key)


	if start_key:
		for i in range(0, start_key):
			csv_f.next()
	else:
		start_key = 0

	try:
		rows_read = 0
		for row in csv_f:
			i = 0
			new_dp = DatoCNBV()
			raw_dp = row[0].split(',')
			for a_key in attributes:
				a_val = raw_dp[i]

				if a_key in ['extraccion', 'cve_periodo', 'cve_institucion', 'cve_TEC', 'cve_dato']:
					setattr(new_dp, a_key, int(a_val))
				elif a_key in ['archivo_fuente', 'dl_institucion', 'dl_dato', 'dl_TEC']:
					setattr(new_dp, a_key, (a_val.decode('utf-8')).encode('utf-8'))
				elif a_key in ['saldo']:
					setattr(new_dp, a_key, float(a_val))		
				
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
		print
		print "Con este valor entra rows read a la excepcion"
		print rows_read
		# print 'Ya fue el DeadLineExceededError'
		deferred.defer(load_cnbv_csv, blob_key, start_key + rows_read)
		return
	return






class CsvUploadFormHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/upload_csv')
        # To upload files to the blobstore, the request method must be "POST"
        # and enctype must be set to "multipart/form-data".
        self.response.out.write("""
			<html><body>
			<form action="{0}" method="POST" enctype="multipart/form-data">
			  Upload File: <input type="file" name="file"><br>
			  <input type="submit" name="submit" value="Submit">
			</form>
			</body></html>""".format(upload_url))


class CsvUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		upload = self.get_uploads()[0]
		csv_file = CsvFile(
			file_name='Test upload 01',
			blob_key=upload.key())
		csv_file.put()		
		# self.load_cnbv_csv(upload.key())
		# self.redirect('/')

		self.redirect('/LoadCSV?blob_key=%s' % upload.key())
	def load_cnbv_csv(self, blob_key):
		blob_reader = blobstore.BlobReader(blob_key)
		csv_f = csv.reader(blob_reader, dialect=csv.excel_tab)
		attributes = csv_f.next()[0].decode('utf-8-sig').split(',') #.decode('utf-8-sig').
		print
		print 'Estos son los attributos'
		print attributes
		print
		for row in csv_f:
			new_dp = DatoCNBV()
			i = 0
			raw_dp = row[0].split(',')
			for a_key in attributes:
				a_val = raw_dp[i]

				if a_key in ['extraccion', 'cve_periodo', 'cve_institucion', 'cve_TEC', 'cve_dato']:
					setattr(new_dp, a_key, int(a_val))
				elif a_key in ['archivo_fuente', 'dl_institucion', 'dl_dato', 'dl_TEC']:
					setattr(new_dp, a_key, (a_val.decode('utf-8')).encode('utf-8'))
				elif a_key in ['saldo']:
					setattr(new_dp, a_key, float(a_val))		
				
				i += 1	
				if i % 100 == 0:
					print i
			new_dp.put()
		return





app = webapp2.WSGIApplication([
    ('/', ChartViewer),
    ('/ChartViewer', ChartViewer),
    ('/CNBVQueries',CNBVQueries),
    ('/LoadCSV', LoadCSV),
    ('/CsvUploadFormHandler', CsvUploadFormHandler),
    ('/upload_csv', CsvUploadHandler)
], debug=True)


