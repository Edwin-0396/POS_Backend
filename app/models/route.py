from app import db
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON

class Route(db.Model):
    __tablename__ = 'route'

    id_route = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    id_administrator = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=True)

    checkin_history = db.Column(JSON, nullable=True)  # Array of GPS coordinates and timestamps
    checkout_history = db.Column(JSON, nullable=True)

    administrator = relationship('User', foreign_keys=[id_administrator], back_populates='routes')
    salesperson = relationship('User', foreign_keys=[id_salesperson], back_populates='routes')
    form = relationship('Form', back_populates='routes')

    def __repr__(self):
        return f'<Route {self.route_name}>'
