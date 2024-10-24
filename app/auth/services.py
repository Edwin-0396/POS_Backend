from .models import User
from app import db, bcrypt

def create_user(data):
    user = User(
        name=data['name'],
        email=data['email'],
        role=data['role'],
    )
    user.set_password(data['password'])
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return None

def authenticate_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        return user
    return None
