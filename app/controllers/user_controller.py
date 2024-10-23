from flask import request, jsonify
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserController:
    
    def register_user():
        data = request.get_json()
        new_user = User(
            email=data['email'],
            password=generate_password_hash(data['password'])
        )
        # Add to database logic here
        return jsonify({"message": "User registered successfully!"}), 201

    def login_user():
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid credentials"}), 401

    def get_user(id_usuario):
        # Logic to get user details
        pass
