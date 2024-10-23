from flask import request, jsonify
from app.services.geolocation_service import GeolocationService

class GeolocationController:

    def record_geolocation(self):
        data = request.get_json()
        location = GeolocationService.record_geolocation(data)
        return jsonify({"message": "Location recorded", "location": location}), 201

    def get_geolocations_by_route(self, id_ruta):
        locations = GeolocationService.get_geolocations_by_route(id_ruta)
        return jsonify(locations), 200
