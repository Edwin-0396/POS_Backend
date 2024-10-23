from flask import Blueprint
from app.controllers.user_controller import UserController
from app.middleware.auth_middleware import authenticate
from app.middleware.role_middleware import authorize
from app.controllers.login_controller import login

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/login', methods=['POST'])
def login_route():
    return login()

# Register a new user
@user_routes.route('/users/register', methods=['POST'])
def register_user():
    return UserController().register_user()

# User login
@user_routes.route('/users/login', methods=['POST'])
def login_user():
    return UserController().login_user()

# Get user details (requires authentication)
@user_routes.route('/users/<int:id_usuario>', methods=['GET'])
@authenticate
def get_user_details(current_user, id_usuario):
    return UserController().get_user_details(id_usuario)

# Assign a route to a user (requires admin privileges)
@user_routes.route('/users/<int:id_usuario>/assign_route/<int:id_ruta>', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def assign_route(current_user, id_usuario, id_ruta):
    return UserController().assign_route(id_usuario, id_ruta)

# Dashboard access (supervisors and administrators only)
@user_routes.route('/users/<int:id_usuario>/dashboard', methods=['GET'])
@authenticate
@authorize(['Administrador', 'Supervisora'])
def get_dashboard_access(current_user, id_usuario):
    return UserController().get_dashboard_access(id_usuario)
