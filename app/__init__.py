from flask import Flask
from .config import Config  
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap

# Inicializar el objeto flask 
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


# Iniciar el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registrar modulos(Blueprints)

app.register_blueprint(mi_blueprint) 
app.register_blueprint(productos)


# LLAMAR A LOS MODELOS

from .models import Cliente, Venta, Producto, Detalles