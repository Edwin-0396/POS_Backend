from flask import request, jsonify
from functools import wraps
from app.utils.jwt_utils import decode_token
from app.services.user_service import UserService

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            decoded_token = decode_token(token)
            current_user = UserService.get_user_by_id(decoded_token['user_id'])
        except Exception as e:
            return jsonify({"message": "Invalid token!"}), 401
        return f(current_user, *args, **kwargs)
    return decorated_function
