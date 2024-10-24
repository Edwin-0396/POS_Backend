from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Use environment variables for database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('POS_BACKEND_SECRET_KEY')

db = SQLAlchemy(app)  # Important: Initialize with the app
migrate = Migrate(app, db)

# Import your models after initializing db
from models import User

@app.route('/')
def index():
    return "Hello from POS_Backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
