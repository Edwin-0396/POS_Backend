from app.models.geolocation import Geolocation
from app import db

class GeolocationService:

    @staticmethod
    def record_geolocation(data):
        new_geolocation = Geolocation(
            id_salesperson=data['id_salesperson'],
            id_route=data['id_route'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            timestamp=data['timestamp']
        )
        db.session.add(new_geolocation)
        db.session.commit()
        return new_geolocation

    @staticmethod
    def get_geolocations_by_route(id_route):
        return Geolocation.query.filter_by(id_route=id_route).all()
