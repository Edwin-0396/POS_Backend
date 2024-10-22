from app import app, db
from flask import jsonify, request
from app.models import Route

@app.route('/routes', methods=['GET'])
def get_routes():
    routes = Route.query.all()
    return jsonify([{"id": r.id_route, "name": r.name_route, "admin_id": r.id_admin, "salesperson_id": r.id_salesperson} for r in routes])

@app.route('/routes', methods=['POST'])
def create_route():
    data = request.json
    new_route = Route(
        name_route=data['name_route'], 
        id_admin=data['id_admin'], 
        id_salesperson=data['id_salesperson'], 
        checkin_history=[], 
        checkout_history=[]
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify({"message": "Route created successfully"}), 201
