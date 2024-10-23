from app import db
from sqlalchemy.dialects.postgresql import JSON

class FormResponse(db.Model):
    __tablename__ = 'form_response'

    id_form_response = db.Column(db.Integer, primary_key=True)
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    id_route = db.Column(db.Integer, db.ForeignKey('route.id_route'), nullable=False)
    id_form = db.Column(db.Integer, db.ForeignKey('form.id_form'), nullable=False)

    responses = db.Column(JSON, nullable=False)  # Array of form responses
    photo = db.Column(db.String(255), nullable=True)
    geolocation = db.Column(JSON, nullable=False)  # GPS coordinates
    checkin_datetime = db.Column(db.DateTime, nullable=False)
    checkout_datetime = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<FormResponse {self.id_form_response}>'
