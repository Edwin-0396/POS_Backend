from flask import Blueprint
from app.controllers.geolocation_controller import GeolocationController
from app.middleware.auth_middleware import authenticate

geolocation_routes = Blueprint('geolocation_routes', __name__)

# Record geolocation for a salesperson on a route
@geolocation_routes.route('/geolocations', methods=['POST'])
@authenticate
def record_geolocation(current_user):
    return GeolocationController().record_geolocation()

# Get all geolocations for a specific route
@geolocation_routes.route('/geolocations/route/<int:id_ruta>', methods=['GET'])
@authenticate
def get_geolocations_by_route(current_user, id_ruta):
    return GeolocationController().get_geolocations_by_route(id_ruta)
