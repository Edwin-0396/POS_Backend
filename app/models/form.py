from app import db
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON

class Form(db.Model):
    __tablename__ = 'form'

    id_form = db.Column(db.Integer, primary_key=True)
    form_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    id_administrator = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)

    fields = db.Column(JSON, nullable=False)  # Array of input definitions (e.g., text, number, checkbox)

    administrator = relationship('User', back_populates='forms')
    routes = relationship('Route', back_populates='form')

    def __repr__(self):
        return f'<Form {self.form_name}>'
