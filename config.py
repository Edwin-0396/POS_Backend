from dotenv import load_dotenv
import os

load_dotenv()  # This will load the .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://pos_user:pos_password@localhost/pos_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
