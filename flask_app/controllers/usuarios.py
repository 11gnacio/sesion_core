from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
	if 'usuario_id' in session:
		return redirect('/dashboard')
	return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registrar_usuario():
	if not Usuario.validar_registro(request.form):
		return redirect('/')

	pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

	data = {
		'nombre': request.form['nombre'],
		'apellido': request.form['apellido'],
		'email': request.form['email'],
		'password': pw_hash
	}

	usuario_id = Usuario.save(data)
	session['usuario_id'] = usuario_id
	return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
	usuario_db = Usuario.get_by_email({'email': request.form['email']})

	if not usuario_db:
		flash("Correo o contraseña incorrectos.", "login")
		return redirect('/')

	if not bcrypt.check_password_hash(usuario_db.password, request.form['password']):
		flash("Correo o contraseña incorrectos.", "login")
		return redirect('/')

	session['usuario_id'] = usuario_db.id
	return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
	if 'usuario_id' not in session:
		return redirect('/')

	usuario = Usuario.get_by_id({'id': session['usuario_id']})
	return render_template('dashboard.html', usuario=usuario)

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')
