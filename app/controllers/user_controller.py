from flask import request, jsonify
from app.services.user_service import UserService
from app.utils.jwt_utils import generate_token

class UserController:
    
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
