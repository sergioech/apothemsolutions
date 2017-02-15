# -*- coding: utf-8 -*-

#--- Definiciones y opciones ---
def_tipo_valor = {
	'01': 'Cartera total',
	'02': 'Cartera vigente',
	'03': 'Cartera vencida',
	'04': 'Número de créditos',
	'05': 'Número de acreditados',
	'21': 'Tasa de interés MN',
	'22': 'Tasa de interés ME',
	'23': 'Tasa de interés UDIS',
	'51': 'Plazo ponderado en meses (remanente)'
}

cat_variables = {
	'01': 'saldo_total',
	'02': 'car_vigente',
	'03': 'car_vencida',
	'04': 'creditos',
	'05': 'acreditados',
	'21': 'tasa_i_mn',
	'22': 'tasa_i_me',
	'23': 'tasa_i_udis',
	'51': 'plazo_ponderado'
}

def_variables  = {
	'saldo_total': 'Cartera total'.decode('utf-8'),
	'car_vigente': 'Cartera vigente'.decode('utf-8'),
	'car_vencida': 'Cartera vencida'.decode('utf-8'),
	'creditos': 'Número de créditos'.decode('utf-8'),
	'acreditados': 'Número de acreditados'.decode('utf-8'),
	'tasa_i_mn': 'Tasa de interés MN'.decode('utf-8'),
	'tasa_i_me': 'Tasa de interés ME'.decode('utf-8'),
	'tasa_i_udis': 'Tasa de interés UDIS'.decode('utf-8'),
	'plazo_ponderado': 'Plazo ponderado en meses (remanente)'.decode('utf-8')
}

opc_variables = [
	'saldo_total',
	'car_vigente',
	'car_vencida',
	'creditos',
	'acreditados',
	'tasa_i_mn',
	'tasa_i_me',
	'tasa_i_udis',
	'plazo_ponderado'
]

def_cortes = {
	'periodo': 'Periodo'.decode('utf-8'),
	'institucion': 'Banco'.decode('utf-8'),
	'estado': 'Entidad Federativa'.decode('utf-8'),
	'tec': 'Tamaño de Empresa'.decode('utf-8')
}

opc_cortes = [
	'periodo',
	'institucion',
	'estado',
	'tec'
]



def decode_options(options_list):
	result = []
	for opcion in options_list:
		result.append([opcion[0].decode('utf-8'), opcion[1].decode('utf-8')])
	return result



opc_tipo_valor = [
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


def_periodo = {
	201601: '201601',
	201602: '201602',
	201603: '201603',
	201604: '201604',
	201605: '201605',
	201606: '201606',
	201607: '201607',
	201608: '201608',
	201609: '201609',
	201610: '201610',
	201611: '201611'
}


opc_periodo = [
	['201601', '201601'],
	['201602', '201602'],
	['201603', '201603'],
	['201604', '201604'],
	['201605', '201605'],
	['201606', '201606'],
	['201607', '201607'],
	['201608', '201608'],
	['201609', '201609'],
	['201610', '201610'],
	['201611', '201611']
]


definiciones = {
	'tipo_valor':def_tipo_valor,
	'institucion':def_institucion, 
	'tec':def_tec,
	'estado': def_estado,
	'periodo': def_periodo,
	'variables': def_variables,
	'cortes': def_cortes
}


opciones = {
	'tipo_valor': decode_options(opc_tipo_valor),
	'institucion': decode_options(opc_institucion),
	'tec': decode_options(opc_tec),
	'estado': decode_options(opc_estado),
	'periodo': decode_options(opc_periodo)
}




#--- Catalogos CNBV ---
cat_institucion = {
	'5': ['Total Banca Múltiple', '00'],
	'040138': ['ABC Capital', '11'],
	'040133': ['Actinver', '12'],
	'040062': ['Afirme', '13'],
	'040103': ['American Express', '14'],
	'040128': ['Autofin', '15'],
	'040002': ['Banamex', '16'],
	'040042': ['Banca Mifel', '17'],
	'040131': ['Banco Ahorro Famsa', '18'],
	'040127': ['Banco Azteca', '19'],
	'040152': ['Banco Bancrea', '20'],
	'040145': ['Banco Base', '21'],
	'040146': ['Banco Bicentenario', '22'],
	'040126': ['Banco Credit Suisse', '23'],
	'040030': ['Banco del Bajío', '24'],
	'040156': ['Banco Sabadell', '25'],
	'040134': ['Banco Wal-Mart', '26'],
	'040137': ['BanCoppel', '27'],
	'040106': ['Bank of America', '28'],
	'040108': ['Bank of Tokyo-Mitsubishi UFJ', '29'],
	'040147': ['Bankaool', '30'],
	'040072': ['Banorte/Ixe', '31'],
	'040058': ['Banregio', '32'],
	'040060': ['Bansí', '33'],
	'040012': ['BBVA Bancomer', '34'],
	'040143': ['CIBanco', '35'],
	'040140': ['Consubanco', '36'],
	'040124': ['Deutsche Bank', '37'],
	'040151': ['Dondé Banco', '38'],
	'040154': ['Finterra', '39'],
	'040021': ['HSBC', '40'],
	'040155': ['ICBC', '41'],
	'040036': ['Inbursa', '42'],
	'040116': ['ING', '43'],
	'040150': ['Inmobiliario Mexicano', '44'],
	'040037': ['Interacciones', '45'],
	'040136': ['Intercam Banco', '46'],
	'040102': ['Investa Bank', '47'],
	'040059': ['Invex', '48'],
	'040032': ['Ixe', '49'],
	'040110': ['J.P. Morgan', '50'],
	'040112': ['Monex', '51'],
	'040132': ['Multiva', '52'],
	'040014': ['Santander', '53'],
	'040307': ['Santander Vivienda', '54'],
	'040044': ['Scotiabank', '55'],
	'040113': ['Ve por Más', '56'],

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

detalles_tabla = {
	'040_11A_R4': {'tipo_variables': 'indirectas', 'perspectiva': 'total'},
	'040_11l_R0': {'tipo_variables': 'indirectas', 'perspectiva': 'total'},
	'040_11l_R3': {'tipo_variables': 'directas', 'perspectiva': 'total'}
}


tablas_CNBV = [
	'040_11A_R4',
	'040_11l_R0',
	'040_11l_R3'
]


def generar_indice_CNBV(lista_tablas):
	
	indice_CNBV = []

	campos_variables = ['saldo_total', 'creditos', 'acreditados'] # tipo_valor
	campos_cortes = ['periodo', 'institucion', 'tec', 'estado']

	for tabla in lista_tablas:
		variables = []
		cortes = []
		tm = transformation_maps_CNBV[tabla]		
		for key, value in tm.iteritems():
			attr = value[0]
			if attr in campos_variables:
				variables.append(attr)
			elif attr in campos_cortes:
				cortes.append(attr)
			elif attr == 'tipo_valor':
				for cve, detalle in value[1].iteritems():
					variables.append(cat_variables[detalle[1]])

		indice_CNBV.append([tabla, variables, cortes, detalles_tabla[tabla]['tipo_variables'], detalles_tabla[tabla]['perspectiva']])

	return indice_CNBV


def definir_opciones_iniciales(indice_CNBV):
	variables = []
	cortes = []
	variables_output = []
	cortes_output = []

	for tabla in indice_CNBV:
		variables_tabla = tabla[1]
		cortes_tabla = tabla[2]
		for variable in variables_tabla:
			if variable not in variables:
				variables.append(variable)
				
		for corte in cortes_tabla:
			if corte not in cortes:
				cortes.append(corte)				

	for variable in opc_variables:
		if variable in variables:
			variables_output.append((variable, def_variables[variable]))

	for corte in opc_cortes:
		if corte in cortes:
			cortes_output.append((corte, def_cortes[corte]))

	opciones_validas = {
		'variables': variables_output,
		'cortes': cortes_output
	}

	return opciones_validas
# xx

indice_inicial = generar_indice_CNBV(tablas_CNBV)

opciones_iniciales = definir_opciones_iniciales(indice_inicial)


def invert_dictionary(dictionary):
	result = {}
	for key, value in dictionary.iteritems():
		result[value] = key
	return result

cat_invertida_variables = invert_dictionary(cat_variables)


