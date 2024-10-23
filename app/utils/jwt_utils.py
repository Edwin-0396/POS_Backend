import jwt
import datetime
from flask import current_app

class JWTUtils:

    @staticmethod
    def generate_token(user_id):
        token = jwt.encode({
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token expires in 24 hours
        }, current_app.config['SECRET_KEY'], algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            return None  # Token expired
        except jwt.InvalidTokenError:
            return None  # Invalid token
