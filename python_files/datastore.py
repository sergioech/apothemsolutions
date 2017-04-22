from google.appengine.ext import ndb

#--- datastore classes ----------


class Usuario(ndb.Model):

	#login details
	email = ndb.StringProperty(required=True)
	password_hash = ndb.StringProperty(required=True)

	#user details	
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	
	#tracker fields
	created = ndb.DateTimeProperty(auto_now_add=True)	
	last_modified = ndb.DateTimeProperty(auto_now=True)
	created_by = ndb.KeyProperty()


	@classmethod # This means you can call a method directly on the Class (no on a Class Instance)
	def get_by_usuario_id(cls, usuario_id):
		return Usuario.get_by_id(usuario_id)

	@classmethod
	def get_by_email(cls, email):
		return Usuario.query(Usuario.email == email).get()

	@classmethod
	def valid_login(cls, email, password):
		usuario = cls.get_by_email(email)
		if usuario and validate_password(email, password, usuario.password_hash):
			return usuario




class TablaCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	nombre = ndb.StringProperty(required=True)
	descripcion = ndb.StringProperty(required=True)
	url_fuente = ndb.StringProperty()
	unidades = ndb.JsonProperty()
	registros = ndb.IntegerProperty(default=0)
	diccionarios = ndb.JsonProperty()


class CsvCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	blob_key = ndb.BlobKeyProperty(required=True)
	Key_TablaCNBV = ndb.KeyProperty(kind=TablaCNBV, required=True)	
	nombre_tablaCNBV =  ndb.StringProperty(required=True)
	nombre = ndb.StringProperty()
	covertura = ndb.JsonProperty()
	rows_transfered = ndb.IntegerProperty(default=0)


class DatoCNBV(ndb.Model):
	
	created = ndb.DateTimeProperty(auto_now_add=True)
	tabla = ndb.KeyProperty(kind=TablaCNBV, required=True)	
	archivo_fuente = ndb.KeyProperty(kind=CsvCNBV, required=True)
		
	periodo = ndb.IntegerProperty()
	institucion = ndb.StringProperty()
	tec = ndb.StringProperty()
	estado = ndb.StringProperty()	
	cliente = ndb.StringProperty()
	moneda = ndb.StringProperty()
	intervalo = ndb.StringProperty()
	
	#Formato vertical
	tipo_valor = ndb.StringProperty()
	valor = ndb.FloatProperty()
	
	#Formato horizontal
	saldo_total = ndb.FloatProperty()
	creditos = ndb.FloatProperty()
	acreditados = ndb.FloatProperty()
	tasa = ndb.FloatProperty()
	plazo = ndb.FloatProperty()
	imor = ndb.FloatProperty()

	saldo_acum = ndb.FloatProperty()
	porc_acum = ndb.FloatProperty()


	