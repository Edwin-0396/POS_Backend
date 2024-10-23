from flask import Blueprint
from app.controllers.role_controller import RoleController
from app.middleware.auth_middleware import authenticate

role_routes = Blueprint('role_routes', __name__)

# Get all roles
@role_routes.route('/roles', methods=['GET'])
@authenticate
def get_roles(current_user):
    return RoleController().get_roles()

# Assign a role to a user (requires admin privileges)
@role_routes.route('/roles/<int:id_usuario>/assign/<int:id_rol>', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def assign_role_to_user(current_user, id_usuario, id_rol):
    return RoleController().assign_role_to_user(id_usuario, id_rol)
