from flask import Blueprint
from app.controllers.route_controller import RouteController
from app.middleware.auth_middleware import authenticate
from app.middleware.role_middleware import authorize

route_routes = Blueprint('route_routes', __name__)

# Create a new route (requires admin privileges)
@route_routes.route('/routes', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def create_route(current_user):
    return RouteController().create_route()

# Assign a salesperson to a route (requires admin privileges)
@route_routes.route('/routes/<int:id_ruta>/assign_salesperson/<int:id_vendedora>', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def assign_salesperson_to_route(current_user, id_ruta, id_vendedora):
    return RouteController().assign_vendedora_to_route(id_ruta, id_vendedora)

# Record a checkin for a route
@route_routes.route('/routes/<int:id_ruta>/checkin', methods=['POST'])
@authenticate
def record_checkin(current_user, id_ruta):
    checkin_data = request.get_json()
    return RouteController().record_checkin(id_ruta, checkin_data)

# Record a checkout for a route
@route_routes.route('/routes/<int:id_ruta>/checkout', methods=['POST'])
@authenticate
def record_checkout(current_user, id_ruta):
    checkout_data = request.get_json()
    return RouteController().record_checkout(id_ruta, checkout_data)
