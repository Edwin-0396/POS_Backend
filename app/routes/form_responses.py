from app import app, db
from flask import jsonify, request
from app.models import FormResponse

@app.route('/form_responses', methods=['GET'])
def get_form_responses():
    responses = FormResponse.query.all()
    return jsonify([{
        "id": r.id_form_response, 
        "salesperson_id": r.id_salesperson, 
        "route_id": r.id_route, 
        "form_id": r.id_form, 
        "responses": r.responses, 
        "photo": r.photo, 
        "geolocation": r.geolocation
    } for r in responses])

@app.route('/form_responses', methods=['POST'])
def create_form_response():
    data = request.json
    new_response = FormResponse(
        id_salesperson=data['id_salesperson'],
        id_route=data['id_route'], 
        id_form=data['id_form'], 
        responses=data['responses'], 
        photo=data['photo'], 
        geolocation=data['geolocation'],
        checkin_time=data['checkin_time'], 
        checkout_time=data['checkout_time']
    )
    db.session.add(new_response)
    db.session.commit()
    return jsonify({"message": "Form response created successfully"}), 201
