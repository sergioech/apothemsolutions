from google.appengine.ext import ndb

#--- datastore classes ----------

class DatoCNBV(ndb.Model):
	
	created = ndb.DateTimeProperty(auto_now_add=True)	
	archivo_fuente = ndb.StringProperty(required=True)
	extraccion = ndb.IntegerProperty(required=True)

	#Aparecen en: 040_11l_R0
	cve_periodo = ndb.IntegerProperty()
	cve_institucion = ndb.IntegerProperty()
	cve_TEC = ndb.IntegerProperty()
	cve_dato = ndb.IntegerProperty()
	saldo = ndb.FloatProperty()
	
	dl_institucion = ndb.StringProperty()
	dl_dato = ndb.StringProperty()
	dl_TEC = ndb.StringProperty()
