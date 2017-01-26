from google.appengine.ext import ndb

#--- datastore classes ----------

class TablaCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	nombre = ndb.StringProperty(required=True)
	descripcion = ndb.StringProperty(required=True)
	url_fuente = ndb.StringProperty()
	unidades = ndb.JsonProperty()
	registros = ndb.IntegerProperty()
	diccionarios = ndb.JsonProperty()


class CsvCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	blob_key = ndb.BlobKeyProperty()
	Key_TablaCNBV = ndb.KeyProperty(kind=TablaCNBV)	
	nombre = ndb.StringProperty()
	covertura = ndb.JsonProperty()
	rows_transfered = ndb.IntegerProperty()


class DatoCNBV(ndb.Model):
	
	created = ndb.DateTimeProperty(auto_now_add=True)
	tabla = ndb.KeyProperty(kind=TablaCNBV, required=True)	
	archivo_fuente = ndb.KeyProperty(kind=CsvCNBV, required=True)
		
	periodo = ndb.IntegerProperty()
	institucion = ndb.StringProperty()
	tec = ndb.StringProperty()
	estado = ndb.StringProperty()

	#Formato vertical
	tipo_valor = ndb.StringProperty()
	valor = ndb.FloatProperty()
	
	#Formato horizontal
	saldo_total = ndb.FloatProperty()
	creditos = ndb.FloatProperty()
	acreditados = ndb.FloatProperty()



	