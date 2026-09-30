from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')

class Usuario:
	DB = "esquema_loginreg"

	def __init__(self, data):
		self.id = data['id']
		self.nombre = data['nombre']
		self.apellido = data['apellido']
		self.email = data['email']
		self.password = data['password']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

	@classmethod
	def save(cls, data):
		query = """
			INSERT INTO usuarios (nombre, apellido, email, password)
			VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
		"""
		return connectToMySQL(cls.DB).query_db(query, data)

	@classmethod
	def get_by_email(cls, data):
		query = "SELECT * FROM usuarios WHERE email = %(email)s;"
		result = connectToMySQL(cls.DB).query_db(query, data)
		if len(result) < 1:
			return False
		return cls(result[0])

	@classmethod
	def get_by_id(cls, data):
		query = "SELECT * FROM usuarios WHERE id = %(id)s;"
		result = connectToMySQL(cls.DB).query_db(query, data)
		if len(result) < 1:
			return False
		return cls(result[0])

	@staticmethod
	def validar_registro(usuario):
		is_valid = True

		# Validar Nombre
		if len(usuario['nombre'].strip()) < 2:
			flash("El nombre debe tener al menos 2 caracteres.", "registro")
			is_valid = False
		elif not NOMBRE_REGEX.match(usuario['nombre']):
			flash("El nombre solo debe contener letras.", "registro")
			is_valid = False

		# Validar Apellido
		if len(usuario['apellido'].strip()) < 2:
			flash("El apellido debe tener al menos 2 caracteres.", "registro")
			is_valid = False
		elif not NOMBRE_REGEX.match(usuario['apellido']):
			flash("El apellido solo debe contener letras.", "registro")
			is_valid = False

		# Validar Email
		if not EMAIL_REGEX.match(usuario['email']):
			flash("Dirección de correo electrónico inválida.", "registro")
			is_valid = False
		elif Usuario.get_by_email({'email': usuario['email']}):
			flash("El correo electrónico ya está registrado.", "registro")
			is_valid = False

		# Validar Contraseña
		if len(usuario['password']) < 8:
			flash("La contraseña debe tener al menos 8 caracteres.", "registro")
			is_valid = False

		if usuario['password'] != usuario['confirm_password']:
			flash("Las contraseñas no coinciden.", "registro")
			is_valid = False

		return is_valid
