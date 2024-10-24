from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config  # Import the config object directly

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)  # Load the simplified config directly

    db.init_app(app)
    migrate.init_app(app, db)

    # Import the models only after the app and db are initialized
    from app.models.user import User

    return app
