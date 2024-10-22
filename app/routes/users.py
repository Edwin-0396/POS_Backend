from app import app, db
from flask import jsonify, request
from app.models import User

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id_user, "name": u.name, "email": u.email, "role": u.role} for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        name=data['name'], 
        email=data['email'], 
        password=data['password'], 
        phone=data['phone'], 
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201
