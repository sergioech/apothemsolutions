# -*- coding: utf-8 -*-

dl_institucion = {
	'5': 'Total Banca Múltiple',
	'040138': 'ABC Capital',
	'040133': 'Actinver',
	'040062': 'Afirme',
	'040103': 'American Express',
	'040128': 'Autofin',
	'040002': 'Banamex',
	'040042': 'Banca Mifel',
	'040131': 'Banco Ahorro Famsa',
	'040127': 'Banco Azteca',
	'040152': 'Banco Bancrea',
	'040145': 'Banco Base',
	'040146': 'Banco Bicentenario',
	'040126': 'Banco Credit Suisse',
	'040030': 'Banco del Bajío',
	'040156': 'Banco Sabadell',
	'040134': 'Banco Wal-Mart',
	'040137': 'BanCoppel',
	'040106': 'Bank of America',
	'040108': 'Bank of Tokyo-Mitsubishi UFJ',
	'040147': 'Bankaool',
	'040072': 'Banorte/Ixe',
	'040058': 'Banregio',
	'040060': 'Bansí',
	'040012': 'BBVA Bancomer',
	'040143': 'CIBanco',
	'040140': 'Consubanco',
	'040124': 'Deutsche Bank',
	'040151': 'Dondé Banco',
	'040154': 'Finterra',
	'040021': 'HSBC',
	'040155': 'ICBC',
	'040036': 'Inbursa',
	'040116': 'ING',
	'040150': 'Inmobiliario Mexicano',
	'040037': 'Interacciones',
	'040136': 'Intercam Banco',
	'040102': 'Investa Bank',
	'040059': 'Invex',
	'040032': 'Ixe',
	'040110': 'J.P. Morgan',
	'040112': 'Monex',
	'040132': 'Multiva',
	'040014': 'Santander',
	'040307': 'Santander Vivienda',
	'040044': 'Scotiabank',
	'040113': 'Ve por Más'
}

dl_dato = {
	'3': '1. Número de Créditos',
	'4': '0. Número de Acreditados',
	'0': '2. Cartera Total',
	'1': '3. Cartera Vigente',
	'2': '4. Cartera Vencida',
}

dl_concepto = {
	'1': 'Número de Créditos',
	'2': 'Número de Acreditados',
	'3': 'Tasa de Interés MN',
	'6': 'Plazo Ponderado en meses (remanente)',
	'7': 'Responsabilidad Total',
	'4': 'Tasa de Interés ME',
	'5': 'Tasa de Interés UDIS'
}

dl_TEC = {
	'1': 'Micro',
	'2': 'Pequeña',
	'3': 'Mediana',
	'4': 'Grande',
	'5': 'Fideicomiso',
}

dl_estado = {
	'1': 'Aguascalientes',
	'2': 'Baja California',
	'3': 'Baja California Sur',
	'4': 'Campeche',
	'5': 'Coahuila de Zaragoza',
	'6': 'Colima',
	'7': 'Chiapas',
	'8': 'Chihuahua',
	'9': 'Distrito Federal',
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
	'99': 'Migración',
	'999': 'Extranjero'
}


#----
attr_040_11l_R0 = {
	'cve_periodo': 'periodo',
	'cve_institucion': 'institucion',
	'cve_TEC': 'tec',
	'cve_dato':'tipo_valor',
	'saldo': 'valor'
}

des_040_11l_R0 = {
	'institucion': dl_institucion,
	'tec': dl_TEC,
	'tipo_valor': dl_dato
}


attr_040_11A_R4 = {
	'cve_institucion': 'institucion',
	'cve_periodo': 'periodo',
	'cve_concepto': 'tipo_valor',
	'dato': 'valor'
}

des_040_11A_R4 = {
	'institucion': dl_institucion,
	'tipo_valor': dl_concepto
}


attr_040_11l_R3 = {
	'cve_periodo': 'periodo',
	'cve_institucion': 'institucion',
	'cve_estado': 'estado',
	'cve_TEC': 'tec',
	'dat_id_credito_met_cnbv': 'creditos',
	'dat_rfc': 'acreditados',
	'dat_responsabilidad_total': 'saldo_total'
}

des_040_11l_R3 = {
	'institucion': dl_institucion,
	'estado': dl_estado,
	'tec': dl_TEC
}


diccionarios_CNBV = {
	'attr_040_11A_R4': attr_040_11A_R4,
	'des_040_11A_R4' : des_040_11A_R4, 

	'attr_040_11l_R0': attr_040_11l_R0,
	'des_040_11l_R0': des_040_11l_R0,

	'attr_040_11l_R3': attr_040_11l_R3,
	'des_040_11l_R3': des_040_11l_R3
}

