from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints
from app.routes.user_routes import user_routes
app.register_blueprint(user_routes)
