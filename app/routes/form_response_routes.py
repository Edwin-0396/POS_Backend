from flask import Blueprint
from app.controllers.form_response_controller import FormResponseController
from app.middleware.auth_middleware import authenticate

form_response_routes = Blueprint('form_response_routes', __name__)

# Submit a form response
@form_response_routes.route('/form_responses', methods=['POST'])
@authenticate
def submit_form_response(current_user):
    return FormResponseController().submit_form_response()

# Get form responses for a specific route
@form_response_routes.route('/form_responses/route/<int:id_ruta>', methods=['GET'])
@authenticate
def get_form_responses_by_route(current_user, id_ruta):
    return FormResponseController().get_form_responses_by_route(id_ruta)
