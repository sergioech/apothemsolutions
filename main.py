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
		self.print_html('ChartViewer.html', variables=variables, cortes=cortes, opciones=opciones)

	def post(self):
		chart_details = json.loads(self.request.body)

		# print
		# print 'This are the chart details: '
		# print chart_details
		# print

		# chart_details['filtros']['periodo'] = list(reversed(chart_details['filtros']['periodo']))

		variable = chart_details['variable']
		corte_renglones = chart_details['renglones']
		perspectiva_portafolio = chart_details['perspectiva_portafolio']
		
		corte_columnas = chart_details['columnas']
		if corte_columnas == 'None':
			corte_columnas = None
 		
		if variable == 'concentracion_cartera':
			corte_renglones = 'cliente'
			
			if chart_details['perspectiva_institucion'] == 'varios_bancos':
				corte_columnas = 'institucion'
			else:
				corte_columnas =  'periodo'
			
			show_value_as = chart_details['show_value_as']
			if show_value_as == 'money':
				variable = 'saldo_acum'
			elif show_value_as == 'percentage':
				variable = 'porc_acum'

			chart_details['filtros']['cliente'] = self.generar_opciones_de_filtro(diccionarios_CNBV.opciones['cliente'])
			# chart_details['filtros']['periodo'] = self.generar_opciones_de_filtro(diccionarios_CNBV.opciones['periodo_y'])

		
		indice_tablas = diccionarios_CNBV.indice_inicial


		# print
		# print 'This is the indice tablas'
		# print indice_tablas
		# print

		nombre_tabla, variables_tabla = self.seleccionar_tabla(variable, corte_renglones, corte_columnas, indice_tablas, perspectiva_portafolio)

		print
		print 'Esta es la tabla seleccionada: ' + nombre_tabla
		print

		key_tabla = TablaCNBV.query(TablaCNBV.nombre == nombre_tabla).get().key
		datos_cnbv = DatoCNBV.query(DatoCNBV.tabla == key_tabla)		
		

		nombre_variable = variable
		tipo_variable = diccionarios_CNBV.detalles_tabla[nombre_tabla]['tipo_variables']		
		
		datos_cnbv = datos_cnbv.filter(DatoCNBV.periodo.IN(self.determinar_rango_periodos(chart_details['filtros']['periodo'])))		
		datos_cnbv = datos_cnbv.filter(DatoCNBV.institucion.IN(chart_details['filtros']['institucion']))

		chart_lead = self.generate_lead(variable, chart_details['filtros']['institucion'], chart_details['filtros']['periodo'], [])
		chart_units = diccionarios_CNBV.def_variables_unidades[variable]

		if tipo_variable == 'indirectas':
			variable = diccionarios_CNBV.cat_invertida_variables[variable]
			datos_cnbv = datos_cnbv.filter(DatoCNBV.tipo_valor == variable)
			variable = 'valor'

		if variable in ['tasa', 'plazo']:
			datos_cnbv = datos_cnbv.filter(DatoCNBV.moneda == chart_details['moneda'])

		datos_cnbv = datos_cnbv.fetch()

		total_dps = len(datos_cnbv)

		datos_cnbv = self.filter_query(datos_cnbv, variables_tabla, chart_details['filtros'])

		chart_array = self.query_to_chart_array(datos_cnbv, variable, corte_renglones, corte_columnas, nombre_variable, chart_details['filtros'])

		print
		print 'This is the chart array'
		print chart_array
		print

		self.response.out.write(json.dumps({
			'chart_array': chart_array,
			'title': chart_lead,
			'chart_units': chart_units,
			'total_dps': total_dps
			}))

		return


	def generate_lead(self, variable, bancos, periodos, cortes):
		definiciones = diccionarios_CNBV.definiciones
		
		variable_lead = definiciones['variables'][variable]
		# variable_lead = definiciones['variables'][variable].decode('utf-8')
		banco_lead = definiciones['institucion'][bancos[0]].decode('utf-8')
		
		if len(bancos) > 1:
			if len(bancos) == 2:
				banco_lead += ' y ' + definiciones['institucion'][bancos[1]].decode('utf-8')
			else:
				banco_lead += ' y otras ' + str(len(bancos) - 1) + ' instituciones ' 
		
	
		periodo_lead =  definiciones['periodo'][int(periodos[0])]

		if len(periodos) == 2:
			periodo_lead += ' y ' + definiciones['periodo'][int(periodos[1])]
		
		elif len(periodos) > 2:
			periodo_lead += ' y otros ' + str(len(periodos) - 1) + ' periodos ' 

		lead = variable_lead + ' de ' + banco_lead + ' durante ' + periodo_lead
		return lead	

	def define_chart_units(self, variable):
		units = 'Millones de pesos ($MXN)'
		return units


	def determinar_rango_periodos(self, opciones_periodos):
		result = []
		for opcion in opciones_periodos:
			result.append(int(opcion))

		return result

		#xx
	def seleccionar_tabla(self, variable, corte_renglones, corte_columnas, indice_tablas, perspectiva_portafolio):

		new_indice_tablas = []

		for tabla in indice_tablas:
			if tabla[4] == perspectiva_portafolio:
				new_indice_tablas.append(tabla)

		indice_tablas = new_indice_tablas

		if corte_columnas:
			for tabla in indice_tablas:
				variables_validas = tabla[1]
				cortes_validos = tabla[2]
				if variable in variables_validas and corte_renglones in cortes_validos and corte_columnas in cortes_validos:
					return tabla[0], cortes_validos
		else:
			for tabla in indice_tablas:
				variables_validas = tabla[1]
				cortes_validos = tabla[2]
				if variable in variables_validas and corte_renglones in cortes_validos:
					return tabla[0], cortes_validos

		return None, None


	def options_to_chart_array(self, rows_options, column_options, rows_title,  variable_name, valid_row_options, valid_column_options, corte_columnas, corte_renglones): #, corte_columnas, corte_renglones
		
		array_headings = [rows_title]
		columns_position = {}
		rows_position = {}


		if column_options:
			col = 1
			for column in column_options:
				if str(column[0]) in valid_column_options:
					if corte_columnas == 'periodo':
						array_headings.append(int(column[0]))
						columns_position[int((column[0]))] = col
					else:
						array_headings.append(column[0])
						columns_position[column[0]] = col
					col += 1
		else:
			array_headings.append(variable_name)

		numero_columnas = len(array_headings)
		chart_array = [array_headings]
		reng = 1
		for row in rows_options:
			if str(row[0]) in valid_row_options:
				if corte_renglones == 'periodo':
					new_row = [int(row[0])]
					rows_position[int(row[0])] = reng
				else:
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

	def query_to_chart_array(self, query_result, variable, corte_renglones, corte_columnas, nombre_variable, diccionario_filtros):

		opciones = diccionarios_CNBV.opciones
		definiciones =  diccionarios_CNBV.definiciones

		row_options = opciones[corte_renglones]
		valid_row_options = diccionario_filtros[corte_renglones]
		row_definitions = definiciones[corte_renglones]
		
		column_options = None
		valid_column_options = None
		column_definitions = None

		if corte_columnas:
			column_options = opciones[corte_columnas]
			valid_column_options = diccionario_filtros[corte_columnas]
			column_definitions = definiciones[corte_columnas]
		

		chart_array, rows_position, columns_position = self.options_to_chart_array(row_options, column_options, definiciones['cortes'][corte_renglones], definiciones['variables'][nombre_variable], valid_row_options, valid_column_options, corte_columnas, corte_renglones)

		if corte_columnas:
			for dp in query_result:
				chart_array[rows_position[getattr(dp, corte_renglones)]][columns_position[getattr(dp, corte_columnas)]] += getattr(dp, variable) 
		else:
			for dp in query_result:		
				chart_array[rows_position[getattr(dp, corte_renglones)]][1] += getattr(dp, variable) 


		chart_array = self.pimp_chart_array(chart_array, row_definitions, column_definitions)	

		return chart_array


	def filter_query(self, query_result, campos_tabla, diccionario_filtros):

		filtered_query = query_result
		
		for campo in campos_tabla:
			if campo not in ['periodo', 'institucion']:				
				opciones_validas = diccionario_filtros[campo]
				output_filtro = []

				for dp in filtered_query:
					if str(getattr(dp, campo)) in opciones_validas:
						output_filtro.append(dp)
				
				filtered_query = output_filtro

		return filtered_query

	def generar_opciones_de_filtro(self, opciones):
		result = []
		for opcion in opciones:
			result.append(opcion[0])
		return result


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


class PopulateDemoVersion(Handler):

	def get(self):

		tablas = diccionarios_CNBV.tablas_CNBV 
		detalles_demo_tablas = diccionarios_CNBV.demo_version_details

		for tabla in tablas:
			detalles_tabla = detalles_demo_tablas[tabla]
			
			new_table = TablaCNBV(
				nombre = tabla,
				descripcion = detalles_tabla['descripcion'],
				registros = detalles_tabla['registros'],
				url_fuente = detalles_tabla['url_fuente'])
			
			new_table.put()

			test_table = new_table
		
			csv_file = CsvCNBV(
				blob_key=blobstore.blobstore.BlobKey('Ql1fkAqvduYHWhJgXoNKZQ=='),
				Key_TablaCNBV = new_table.key,
				nombre=tabla + '.csv',
				nombre_tablaCNBV=tabla)
			csv_file.put()

			test_csv = csv_file
			load_cnbv_csv(new_table, csv_file, 'from_hard_csv', 0, None, 0)

		self.redirect('/TableViewer')


class CreateAllTables(Handler):

	def get(self):

		tablas = diccionarios_CNBV.tablas_CNBV 
		detalles_demo_tablas = diccionarios_CNBV.demo_version_details

		for tabla in tablas:
			detalles_tabla = detalles_demo_tablas[tabla]
			
			new_table = TablaCNBV(
				nombre = tabla,
				descripcion = detalles_tabla['descripcion'],
				registros = detalles_tabla['registros'],
				url_fuente = detalles_tabla['url_fuente'])
			new_table.put()

		self.redirect('/TableViewer')




class TableViewer(Handler):
	def get(self):
		tablas_cnbv = TablaCNBV.query().order(TablaCNBV.nombre).fetch()
		upload_url = blobstore.create_upload_url('/upload_csv')
		blob_file_input = "{0}".format(upload_url)
		self.print_html('TableViewer.html', tablas_cnbv=tablas_cnbv, blob_file_input=blob_file_input)



class LoadCSV(Handler):
	def get(self):
		tabla_id = self.request.get('tabla_id')
		csv_id = self.request.get('csv_id')

		tabla_cnbv = TablaCNBV.get_by_id(int(tabla_id))
		csv_cnbv = CsvCNBV.get_by_id(int(csv_id))

		load_cnbv_csv(tabla_cnbv, csv_cnbv, 'from_blob', 0, None, 0)
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
def load_cnbv_csv(tabla_cnbv, csv_cnbv, file_source, start_key, max_iterations, iterations_so_far):
	rows_per_iteration = 250

	key_tabla = tabla_cnbv.key
	key_csv = csv_cnbv.key

	if file_source == 'from_blob':
		blob_key = csv_cnbv.blob_key
		blob_reader = blobstore.BlobReader(blob_key)
		csv_f = csv.reader(blob_reader, dialect=csv.excel_tab)

	elif file_source == 'from_hard_csv':	
		csv_path = os.path.join(os.path.dirname(__file__), 'csv_files', tabla_cnbv.nombre + '.csv')
		f = open(csv_path, 'rU')
		f.close
		csv_f = csv.reader(f, dialect=csv.excel_tab)

	original_attributes = csv_f.next()[0].decode('utf-8-sig').split(',') 

	tm = diccionarios_CNBV.transformation_maps_CNBV[tabla_cnbv.nombre]
	
	attributes = []
	values_map = {}

	for a in original_attributes:
		attr_map = tm[a]
		attributes.append(attr_map[0])
		if len(attr_map) == 2:
			values_map[attr_map[0]] = attr_map[1]
	
	for i in range(0, start_key):
		csv_f.next()

	rows_read = 0
	for row in csv_f:
		i = 0
		new_dp = DatoCNBV(tabla=key_tabla, archivo_fuente=key_csv)
		raw_dp = row[0].split(',')
		for a_key in attributes:
			a_val = raw_dp[i]
			
			if a_key in ['institucion', 'tec', 'estado', 'tipo_valor', 'cliente', 'moneda', 'intervalo']:				
				setattr(new_dp, a_key, values_map[a_key][a_val.decode('utf-8')][1])					
			
			elif a_key in ['valor', 'saldo_total', 'creditos', 'acreditados', 'saldo_acum', 'porc_acum', 'tasa', 'plazo', 'imor']:
				if a_val == '':
					a_val = '0'
				setattr(new_dp, a_key, float(a_val))		
			
			elif a_key in ['periodo']:
				setattr(new_dp, a_key, int(a_val))
			i += 1				
		new_dp.put()
		rows_read += 1
		if rows_read > rows_per_iteration - 1:			
			break
	iterations_so_far += 1

	renglones_pendientes = sum(1 for row in csv_f)

	if not max_iterations:
		max_iterations = ((renglones_pendientes + rows_read)/rows_per_iteration) + 2

	need_extra_work = False
	if renglones_pendientes > 0 and iterations_so_far < max_iterations:
		need_extra_work = True

	tabla_cnbv.registros += rows_read
	tabla_cnbv.put()

	csv_cnbv.rows_transfered += rows_read
	csv_cnbv.put()

	if need_extra_work:
		deferred.defer(load_cnbv_csv, tabla_cnbv, csv_cnbv, file_source, start_key + rows_read, max_iterations, iterations_so_far)

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
    ('/upload_csv', CsvUploadHandler),
    ('/LoadDemoTables', PopulateDemoVersion),
    ('/CreateAllTables', CreateAllTables)
], debug=True)


