from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    id_role = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id_role'), nullable=False)
    password = db.Column(db.String(512), nullable=False)  # For hashed passwords
    phone = db.Column(db.String(20))
