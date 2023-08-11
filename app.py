#Importaciones del proyecto

from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

#Iniciarlizar el objeto flask 
app = Flask(__name__)
app.config.from_object(Config)

#Iniializar el objeto SQLalchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Modelos - entidades del proyecto 
class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(120), unique = True)

class Ventas(db.Model):
    __tablename__ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class Detalles(db.Model):
    __tablename__ = "detalles"
    id = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)