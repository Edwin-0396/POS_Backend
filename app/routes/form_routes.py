from flask import Blueprint
from app.controllers.form_controller import FormController
from app.middleware.auth_middleware import authenticate
from app.middleware.role_middleware import authorize

form_routes = Blueprint('form_routes', __name__)

# Create a new form (requires admin privileges)
@form_routes.route('/forms', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def create_form(current_user):
    return FormController().create_form()

# Assign a form to a route (requires admin privileges)
@form_routes.route('/forms/<int:id_formulario>/assign/<int:id_ruta>', methods=['POST'])
@authenticate
@authorize(['Administrador'])
def assign_form_to_route(current_user, id_formulario, id_ruta):
    return FormController().assign_form_to_route(id_formulario, id_ruta)
