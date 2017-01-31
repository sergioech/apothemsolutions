# -*- coding: utf-8 -*-

#--- Definiciones y opciones ---
def_tipo_dato = {
	'01': 'Cartera total',
	'02': 'Cartera vigente',
	'03': 'Cartera vencida',
	'04': 'Número de créditos',
	'05': 'Número de acreditados',
	'21': 'Tasa de interés MN',
	'22': 'Tasa de interés ME',
	'23': 'Tasa de interés UDIS',
	'51':'Plazo ponderado en meses (remanente)'
}

opc_tipo_dato = [
	['01', 'Cartera total'],
	['02', 'Cartera vigente'],
	['03', 'Cartera vencida'],
	['04', 'Número de créditos'],
	['05', 'Número de acreditados'],
	['21', 'Tasa de interés MN'],
	['22', 'Tasa de interés ME'],
	['23', 'Tasa de interés UDIS'],
	['51', 'Plazo ponderado en meses (remanente)']
]

def_institucion = {
	'00': 'Total Banca Múltiple',
	'11': 'ABC Capital',
	'12': 'Actinver',
	'13': 'Afirme',
	'14': 'American Express',
	'15': 'Autofin',
	'16': 'Banamex',
	'17': 'Banca Mifel',
	'18': 'Banco Ahorro Famsa',
	'19': 'Banco Azteca',
	'20': 'Banco Bancrea',
	'21': 'Banco Base',
	'22': 'Banco Bicentenario',
	'23': 'Banco Credit Suisse',
	'24': 'Banco del Bajío',
	'25': 'Banco Sabadell',
	'26': 'Banco Wal-Mart',
	'27': 'BanCoppel',
	'28': 'Bank of America',
	'29': 'Bank of Tokyo-Mitsubishi UFJ',
	'30': 'Bankaool',
	'31': 'Banorte/Ixe',
	'32': 'Banregio',
	'33': 'Bansí',
	'34': 'BBVA Bancomer',
	'35': 'CIBanco',
	'36': 'Consubanco',
	'37': 'Deutsche Bank',
	'38': 'Dondé Banco',
	'39': 'Finterra',
	'40': 'HSBC',
	'41': 'ICBC',
	'42': 'Inbursa',
	'43': 'ING',
	'44': 'Inmobiliario Mexicano',
	'45': 'Interacciones',
	'46': 'Intercam Banco',
	'47': 'Investa Bank',
	'48': 'Invex',
	'49': 'Ixe',
	'50': 'J.P. Morgan',
	'51': 'Monex',
	'52': 'Multiva',
	'53': 'Santander',
	'54': 'Santander Vivienda',
	'55': 'Scotiabank',
	'56': 'Ve por Más'
}

opc_institucion = [
	['00',  'Total Banca Múltiple'],
	['11',  'ABC Capital'],
	['12',  'Actinver'],
	['13',  'Afirme'],
	['14',  'American Express'],
	['15',  'Autofin'],
	['16',  'Banamex'],
	['17',  'Banca Mifel'],
	['18',  'Banco Ahorro Famsa'],
	['19',  'Banco Azteca'],
	['20',  'Banco Bancrea'],
	['21',  'Banco Base'],
	['22',  'Banco Bicentenario'],
	['23',  'Banco Credit Suisse'],
	['24',  'Banco del Bajío'],
	['25',  'Banco Sabadell'],
	['26',  'Banco Wal-Mart'],
	['27',  'BanCoppel'],
	['28',  'Bank of America'],
	['29',  'Bank of Tokyo-Mitsubishi UFJ'],
	['30',  'Bankaool'],
	['31',  'Banorte/Ixe'],
	['32',  'Banregio'],
	['33',  'Bansí'],
	['34',  'BBVA Bancomer'],
	['35',  'CIBanco'],
	['36',  'Consubanco'],
	['37',  'Deutsche Bank'],
	['38',  'Dondé Banco'],
	['39',  'Finterra'],
	['40',  'HSBC'],
	['41',  'ICBC'],
	['42',  'Inbursa'],
	['43',  'ING'],
	['44',  'Inmobiliario Mexicano'],
	['45',  'Interacciones'],
	['46',  'Intercam Banco'],
	['47',  'Investa Bank'],
	['48',  'Invex'],
	['49',  'Ixe'],
	['50',  'J.P. Morgan'],
	['51',  'Monex'],
	['52',  'Multiva'],
	['53',  'Santander'],
	['54',  'Santander Vivienda'],
	['55',  'Scotiabank'],
	['56',  'Ve por Más'],
]


def_tec = {
	'01': 'Micro',
	'02': 'Pequeña',
	'03': 'Mediana',
	'04': 'Grande',
	'05': 'Fideicomiso'
}


opc_tec = [
	['01',  'Micro'],
	['02',  'Pequeña'],
	['03',  'Mediana'],
	['04',  'Grande'],
	['05',  'Fideicomiso']
]


def_estado = {
	'01': 'Aguascalientes',
	'02': 'Baja California',
	'03': 'Baja California Sur',
	'04': 'Campeche',
	'05': 'Coahuila de Zaragoza',
	'06': 'Colima',
	'07': 'Chiapas',
	'08': 'Chihuahua',
	'09': 'Distrito Federal',
	'10': 'Durango',
	'11': 'Guanajuato',
	'12': 'Guerrero',
	'13': 'Hidalgo',
	'14': 'Jalisco',
	'15': 'México',
	'16': 'Michoacán de Ocampo',
	'17': 'Morelos',
	'18': 'Nayarit',
	'19': 'Nuevo León',
	'20': 'Oaxaca',
	'21': 'Puebla',
	'22': 'Querétaro',
	'23': 'Quintana Roo',
	'24': 'San Luis Potosí',
	'25': 'Sinaloa',
	'26': 'Sonora',
	'27': 'Tabasco',
	'28': 'Tamaulipas',
	'29': 'Tlaxcala',
	'30': 'Veracruz de Ignacio de la Llave',
	'31': 'Yucatán',
	'32': 'Zacatecas',
	'91': 'Migración',
	'92': 'Extranjero'
}


opc_estado = [
	['01',  'Aguascalientes'],
	['02',  'Baja California'],
	['03',  'Baja California Sur'],
	['04',  'Campeche'],
	['05',  'Coahuila de Zaragoza'],
	['06',  'Colima'],
	['07',  'Chiapas'],
	['08',  'Chihuahua'],
	['09',  'Distrito Federal'],
	['10',  'Durango'],
	['11',  'Guanajuato'],
	['12',  'Guerrero'],
	['13',  'Hidalgo'],
	['14',  'Jalisco'],
	['15',  'México'],
	['16',  'Michoacán de Ocampo'],
	['17',  'Morelos'],
	['18',  'Nayarit'],
	['19',  'Nuevo León'],
	['20',  'Oaxaca'],
	['21',  'Puebla'],
	['22',  'Querétaro'],
	['23',  'Quintana Roo'],
	['24',  'San Luis Potosí'],
	['25',  'Sinaloa'],
	['26',  'Sonora'],
	['27',  'Tabasco'],
	['28',  'Tamaulipas'],
	['29',  'Tlaxcala'],
	['30',  'Veracruz de Ignacio de la Llave'],
	['31',  'Yucatán'],
	['32',  'Zacatecas'],
	['91',  'Migración'],
	['92',  'Extranjero']
]


definiciones = {
	'tipo_dato':def_tipo_dato,
	'institucion':def_institucion, 
	'tec':def_tec,
	'estado': def_estado, 
}


opciones = {
	'tipo_dato': opc_tipo_dato,
	'institucion': opc_institucion,
	'tec': opc_tec,
	'estado': opc_estado
}


def options_to_chart_array(rows_options, column_options):
	
	array_headings = ['Rows title']
	for column in column_options:
		array_headings.append(column[0])

	numero_columnas = len(array_headings)

	chart_array = [array_headings]

	for row in rows_options:
		new_row = [row[0]]
		for i in range(1, numero_columnas):
			new_row.append(0)
		chart_array.append(new_row)	

	return chart_array


def pimp_chart_array(chart_array,rows_definitions, col_definitions):
	pimped_array = []

	pimped_headings = [chart_array[0][0]]

	for heading in chart_array[0][1:]:
		pimped_headings.append(col_definitions[heading])

	pimped_array.append(pimped_headings)

	for row in chart_array[1:]:
		pimped_row = [rows_definitions[row[0]]] + row[1:]
		pimped_array.append(pimped_row)

	return pimped_array



# chart_array = options_to_chart_array(opc_tipo_dato, opc_tec)
# print chart_array
# print




# pimped_array = pimp_chart_array(chart_array, def_tipo_dato, def_tec )
# pimped_array[3][3] += 10
# pimped_array[3][3] += 59 
# print pimped_array


#--- Catalogos CNBV ---
cat_institucion = {
	'5': ['Total Banca Múltiple', '00'],
	'40138': ['ABC Capital', '11'],
	'40133': ['Actinver', '12'],
	'40062': ['Afirme', '13'],
	'40103': ['American Express', '14'],
	'40128': ['Autofin', '15'],
	'40002': ['Banamex', '16'],
	'40042': ['Banca Mifel', '17'],
	'40131': ['Banco Ahorro Famsa', '18'],
	'40127': ['Banco Azteca', '19'],
	'40152': ['Banco Bancrea', '20'],
	'40145': ['Banco Base', '21'],
	'40146': ['Banco Bicentenario', '22'],
	'40126': ['Banco Credit Suisse', '23'],
	'40030': ['Banco del Bajío', '24'],
	'40156': ['Banco Sabadell', '25'],
	'40134': ['Banco Wal-Mart', '26'],
	'40137': ['BanCoppel', '27'],
	'40106': ['Bank of America', '28'],
	'40108': ['Bank of Tokyo-Mitsubishi UFJ', '29'],
	'40147': ['Bankaool', '30'],
	'40072': ['Banorte/Ixe', '31'],
	'40058': ['Banregio', '32'],
	'40060': ['Bansí', '33'],
	'40012': ['BBVA Bancomer', '34'],
	'40143': ['CIBanco', '35'],
	'40140': ['Consubanco', '36'],
	'40124': ['Deutsche Bank', '37'],
	'40151': ['Dondé Banco', '38'],
	'40154': ['Finterra', '39'],
	'40021': ['HSBC', '40'],
	'40155': ['ICBC', '41'],
	'40036': ['Inbursa', '42'],
	'40116': ['ING', '43'],
	'40150': ['Inmobiliario Mexicano', '44'],
	'40037': ['Interacciones', '45'],
	'40136': ['Intercam Banco', '46'],
	'40102': ['Investa Bank', '47'],
	'40059': ['Invex', '48'],
	'40032': ['Ixe', '49'],
	'40110': ['J.P. Morgan', '50'],
	'40112': ['Monex', '51'],
	'40132': ['Multiva', '52'],
	'40014': ['Santander', '53'],
	'40307': ['Santander Vivienda', '54'],
	'40044': ['Scotiabank', '55'],
	'40113': ['Ve por Más', '56']
}

cat_dato = {
	'3': ['1. Número de Créditos', '04'],
	'4': ['0. Número de Acreditados', '05'],
	'0': ['2. Cartera Total', '01'],
	'1': ['3. Cartera Vigente', '02'],
	'2': ['4. Cartera Vencida', '03'],
}

cat_concepto = {
	'1': ['Número de Créditos', '04'],
	'2': ['Número de Acreditados', '05'],
	'3': ['Tasa de Interés MN', '21'],
	'6': ['Plazo Ponderado en meses (remanente)', '51'],
	'7': ['Responsabilidad Total', '01'],
	'4': ['Tasa de Interés ME', '22'],
	'5': ['Tasa de Interés UDIS', '23']
}


cat_TEC = {
	'1': ['Micro', '01'],
	'2': ['Pequeña', '02'],
	'3': ['Mediana', '03'],
	'4': ['Grande', '04'],
	'5': ['Fideicomiso', '05'],
}


cat_estado = {
	'1': ['Aguascalientes', '01'],
	'2': ['Baja California', '02'],
	'3': ['Baja California Sur', '03'],
	'4': ['Campeche', '04'],
	'5': ['Coahuila de Zaragoza', '05'],
	'6': ['Colima', '06'],
	'7': ['Chiapas', '07'],
	'8': ['Chihuahua', '08'],
	'9': ['Distrito Federal', '09'],
	'10': ['Durango', '10'],
	'11': ['Guanajuato', '11'],
	'12': ['Guerrero', '12'],
	'13': ['Hidalgo', '13'],
	'14': ['Jalisco', '14'],
	'15': ['México', '15'],
	'16': ['Michoacán de Ocampo', '16'],
	'17': ['Morelos', '17'],
	'18': ['Nayarit', '18'],
	'19': ['Nuevo León', '19'],
	'20': ['Oaxaca', '20'],
	'21': ['Puebla', '21'],
	'22': ['Querétaro', '22'],
	'23': ['Quintana Roo', '23'],
	'24': ['San Luis Potosí', '24'],
	'25': ['Sinaloa', '25'],
	'26': ['Sonora', '26'],
	'27': ['Tabasco', '27'],
	'28': ['Tamaulipas', '28'],
	'29': ['Tlaxcala', '29'],
	'30': ['Veracruz de Ignacio de la Llave', '30'],
	'31': ['Yucatán', '31'],
	'32': ['Zacatecas', '32'],
	'99': ['Migración', '91'],
	'999': ['Extranjero', '92']
}


#--- trasformation maps ---
tm_040_11A_R4 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],
	'cve_concepto': ['tipo_valor', cat_concepto],
	'dato': ['valor']
}


tm_040_11l_R0 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_TEC': ['tec', cat_TEC],
	'cve_dato':['tipo_valor', cat_dato],
	'saldo': ['valor']
}


tm_040_11l_R3 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_estado': ['estado', cat_estado],
	'cve_TEC': ['tec', cat_TEC],
	'dat_id_credito_met_cnbv': ['creditos'],
	'dat_rfc': ['acreditados'],
	'dat_responsabilidad_total': ['saldo_total']
}


transformation_maps_CNBV = {
	'040_11A_R4': tm_040_11A_R4,
	'040_11l_R0': tm_040_11l_R0,
	'040_11l_R3': tm_040_11l_R3
}

#--- Database Contents
ejemplo_indice = [
	['nombre_tabla_1',
		['valor_1', 'valor_n'],
		['corte_1', 'corte_n']
	],

	['nombre_tabla_n',
		['valor_1', 'valor_n'],
		['corte_1', 'corte_n']
	]
]


def generar_indice_CNBV(lista_tablas):
	
	indice_CNBV = []

	campos_valores = ['valor', 'saldo_total', 'creditos', 'acreditados'] # tipo_valor
	campos_cortes = ['periodo', 'institucion', 'tec', 'estado', 'tipo_valor']


	for tabla in lista_tablas:
		valores = []
		cortes = []
		tm = transformation_maps_CNBV[tabla]		
		for key, value in tm.iteritems():
			attr = value[0]
			if attr in campos_valores:
				valores.append(attr)
			elif attr in campos_cortes:
				cortes.append(attr)

		indice_CNBV.append([tabla, valores, cortes])

	return indice_CNBV


tablas_CNBV = [
	'040_11A_R4',
	# '040_11l_R0',
	# '040_11l_R3'
]

def definir_opciones_validas(indice_CNBV):
	variables = []
	cortes = []

	for tabla in indice_CNBV:
		variables_tabla = tabla[1]
		cortes_tabla = tabla[2]
		for variable in variables_tabla:
			if variable not in variables:
				variables.append(variable)
		for corte in cortes_tabla:
			if corte not in cortes:
				cortes.append(corte)

	opciones_validas = {
		'variables': variables,
		'cortes': cortes
	}

	return opciones_validas


indice_inicial = generar_indice_CNBV(tablas_CNBV)

opciones_iniciales = definir_opciones_validas(indice_inicial)

# print indice_inicial
# print opciones_iniciales

