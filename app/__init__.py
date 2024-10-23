from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt  # Import Flask-Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

# Initialize Flask app
app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config.from_object('app.config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Flask-Bcrypt
bcrypt = Bcrypt(app)

# Import and register routes
from app.routes.users import users_bp
app.register_blueprint(users_bp, url_prefix='/')
