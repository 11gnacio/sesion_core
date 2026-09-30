# 🔐 Registro e Inicio de Sesión Seguro (Flask + MySQL + MVC)

Aplicación web desarrollada con **Flask**, **MySQL** y **Bcrypt** que implementa un sistema seguro de registro, autenticación de usuarios y control de acceso utilizando arquitectura **MVC (Modelo-Vista-Controlador)**.

---

## 🧰 Tecnologías Utilizadas

- **Python 3.x**
- **Flask** (Framework Web)
- **MySQL / MySQL Workbench** (Base de Datos Relacional)
- **PyMySQL** (Conector Python ↔ MySQL)
- **Flask-Bcrypt** (Hashing seguro de contraseñas)
- **python-dotenv** (Manejo de variables de entorno)
- **Bootstrap 5** (Diseño responsivo e interfaz de usuario)
- **Jinja2** (Motor de plantillas HTML)

---

## 📁 Estructura del Proyecto

```text
secure_users/
│
├── flask_app/
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── mysqlconnection.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── usuarios.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── usuario.py
│   │
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       └── index.html
│
├── .env
├── .env.example
├── .gitignore
├── esquema_loginreg.sql
├── Pipfile
├── Pipfile.lock
├── README.md
└── server.py