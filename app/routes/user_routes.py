from flask import Blueprint
from app.controllers.user_controller import UserController

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users/register', methods=['POST'])
def register():
    return UserController.register_user()

@user_routes.route('/users/login', methods=['POST'])
def login():
    return UserController.login_user()

@user_routes.route('/users/<int:id_usuario>', methods=['GET'])
def get_user(id_usuario):
    return UserController.get_user(id_usuario)
