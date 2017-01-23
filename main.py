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

from python_files import datastore, constants
constants = constants.constants

DatoCNBV = datastore.DatoCNBV


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
		file_name = 'mini_040_11l_R0_20170110.csv'
		csv_path = self.create_csv_path(file_name)
		self.load_cnbv_csv(csv_path)
		self.redirect('/ChartViewer')	


	def create_csv_path(self, file_name):
		return os.path.join(os.path.dirname(__file__), 'csv_files', file_name)


	def load_cnbv_csv(self, csv_path):
		f = open(csv_path, 'rU')
		f.close
		csv_f = csv.reader(f, dialect=csv.excel_tab)
		attributes = csv_f.next()[0].decode('utf-8-sig').split(',')
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
			new_dp.put()

		return


app = webapp2.WSGIApplication([
    ('/', ChartViewer),
    ('/ChartViewer', ChartViewer),
    ('/CNBVQueries',CNBVQueries),
    ('/LoadCSV', LoadCSV)
], debug=True)
