from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Role(db.Model):
    id_role = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20))  # Role name: 'Administrator', 'Supervisor', 'Salesperson'

class Route(db.Model):
    id_route = db.Column(db.Integer, primary_key=True)
    name_route = db.Column(db.String(100))
    id_admin = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    checkin_history = db.Column(db.JSON)  # List of check-in GPS coordinates and timestamps
    checkout_history = db.Column(db.JSON)  # List of check-out GPS coordinates and timestamps

class Form(db.Model):
    id_form = db.Column(db.Integer, primary_key=True)
    name_form = db.Column(db.String(100))
    id_admin = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    fields = db.Column(db.JSON)  # Dynamic input fields

class FormResponse(db.Model):
    id_form_response = db.Column(db.Integer, primary_key=True)
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_route = db.Column(db.Integer, db.ForeignKey('route.id_route'))
    id_form = db.Column(db.Integer, db.ForeignKey('form.id_form'))
    responses = db.Column(db.JSON)  # JSON for dynamic form responses
    photo = db.Column(db.String(200))  # URL of the uploaded photo
    geolocation = db.Column(db.JSON)  # GPS coordinates
    checkin_time = db.Column(db.DateTime)
    checkout_time = db.Column(db.DateTime)

class Geolocation(db.Model):
    id_geolocation = db.Column(db.Integer, primary_key=True)
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_route = db.Column(db.Integer, db.ForeignKey('route.id_route'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

class Statistics(db.Model):
    id_statistics = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    total_routes_completed = db.Column(db.Integer)
    avg_checkin = db.Column(db.Float)
    avg_checkout = db.Column(db.Float)
    avg_route_time = db.Column(db.Float)
    completion_percentage = db.Column(db.Float)
