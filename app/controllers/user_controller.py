from flask import request, jsonify
from app.services.user_service import UserService
from app.utils.jwt_utils import generate_token
from app.models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

class UserController:
    def login():
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()

        if user and check_password_hash(user.password, data.get('password')):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    
    def register_user(self):
        data = request.get_json()
        new_user = UserService.create_user(data)
        return jsonify({"message": "User registered successfully", "user": new_user}), 201

    def login_user(self):
        data = request.get_json()
        user = UserService.authenticate(data["correo_electronico"], data["password"])
        if user:
            token = generate_token(user.id_usuario)
            return jsonify({"token": token, "user": user}), 200
        return jsonify({"message": "Invalid credentials"}), 401

    def assign_route(self, id_usuario, id_ruta):
        result = UserService.assign_route(id_usuario, id_ruta)
        if result:
            return jsonify({"message": "Route assigned successfully"}), 200
        return jsonify({"message": "Failed to assign route"}), 400

    def get_dashboard_access(self, id_usuario):
        user = UserService.get_user_by_id(id_usuario)
        if user.rol in ['Administrador', 'Supervisora']:
            return jsonify({"message": "Dashboard Access Granted"}), 200
        return jsonify({"message": "Access Denied"}), 403

    def get_user_details(self, id_usuario):
        user = UserService.get_user_by_id(id_usuario)
        if user:
            return jsonify(user), 200
        return jsonify({"message": "User not found"}), 404
