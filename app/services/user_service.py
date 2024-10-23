from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.jwt_utils import decode_token

class UserService:

    @staticmethod
    def create_user(data):
        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            name=data['name'],
            email=data['email'],
            password_hash=hashed_password,
            phone=data.get('phone'),
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def get_user_by_id(id_user):
        return User.query.get(id_user)

    @staticmethod
    def assign_route(id_user, id_route):
        user = User.query.get(id_user)
        route = Route.query.get(id_route)
        if user and route:
            route.salesperson = user
            db.session.commit()
            return route
        return None
