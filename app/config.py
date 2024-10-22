import os

class Config:
    # Load DATABASE_URL from environment variables, with a default fallback
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:password@db:5432/pos_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable to avoid unnecessary warnings
