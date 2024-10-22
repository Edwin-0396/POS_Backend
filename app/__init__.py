from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importar Flask-Migrate
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


# Inicializar la app Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Cargar la configuración desde config.py
app.config.from_object('app.config.Config')

# Inicializar la base de datos
db = SQLAlchemy(app)

# Inicializar Flask-Migrate
migrate = Migrate(app, db)  # Añadir Flask-Migrate aquí

# Importar rutas después de inicializar app y db para evitar importaciones circulares
from app.routes import users, roles, routes, forms, form_responses, geolocations, statistics
