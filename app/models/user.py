from app import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    role = db.Column(db.String(50), nullable=False)  # (Administrator, Supervisor, Salesperson)

    routes = relationship('Route', back_populates='salesperson')
    forms = relationship('Form', back_populates='administrator')
    statistics = relationship('Statistic', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}>'
