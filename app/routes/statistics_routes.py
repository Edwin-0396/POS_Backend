from flask import Blueprint
from app.controllers.statistics_controller import StatisticsController
from app.middleware.auth_middleware import authenticate

statistics_routes = Blueprint('statistics_routes', __name__)

# Get user statistics
@statistics_routes.route('/statistics/user/<int:id_usuario>', methods=['GET'])
@authenticate
def get_user_statistics(current_user, id_usuario):
    return StatisticsController().get_user_statistics(id_usuario)

# Calculate statistics for a user (requires admin or supervisor privileges)
@statistics_routes.route('/statistics/user/<int:id_usuario>/calculate', methods=['POST'])
@authenticate
def calculate_statistics(current_user, id_usuario):
    return StatisticsController().calculate_statistics(id_usuario)
