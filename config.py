import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://POS_Username:POS_password@localhost:5432/pos_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
