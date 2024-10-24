from werkzeug.security import generate_password_hash
from models import db, User, Role
from app import app

with app.app_context():
    # Check if user already exists
    existing_user = User.query.filter_by(email='POS_user@POS_example.com').first()
    
    if existing_user:
        print("User already exists with this email.")
    else:
        # Hash the password
        hashed_password = generate_password_hash('POS_password', method='pbkdf2:sha256')

        # Find or create the Administrator role
        role = Role.query.filter_by(role_name='Administrator').first()
        if not role:
            role = Role(role_name='Administrator')
            db.session.add(role)
            db.session.commit()

        # Create a new user
        new_user = User(
            name='POS User',
            email='POS_user@POS_example.com',
            password=hashed_password,
            role_id=role.id_role,
            phone='123-456-7890'
        )
        db.session.add(new_user)
        db.session.commit()

        print("User created successfully!")
