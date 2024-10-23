from app import db

class Geolocation(db.Model):
    __tablename__ = 'geolocation'

    id_geolocation = db.Column(db.Integer, primary_key=True)
    id_salesperson = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    id_route = db.Column(db.Integer, db.ForeignKey('route.id_route'), nullable=False)

    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Geolocation {self.id_geolocation}>'
