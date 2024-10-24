import os
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Role
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    role = Role.query.filter_by(role_name='Administrator').first()
    if not role:
        role = Role(role_name='Administrator')
        db.session.add(role)
        db.session.commit()
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role_id=role.id_role,
        phone=data['phone']
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful", "user_id": user.id_user}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    # Vercel uses gunicorn in production
    if os.getenv("VERCEL") == "true":
        app.run(debug=False)
    else:
        app.run(debug=True)
