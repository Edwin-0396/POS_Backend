from app import app, db
from flask import jsonify, request
from app.models import Form

@app.route('/forms', methods=['GET'])
def get_forms():
    forms = Form.query.all()
    return jsonify([{"id": f.id_form, "name": f.name_form, "admin_id": f.id_admin, "fields": f.fields} for f in forms])

@app.route('/forms', methods=['POST'])
def create_form():
    data = request.json
    new_form = Form(
        name_form=data['name_form'], 
        id_admin=data['id_admin'], 
        fields=data['fields']
    )
    db.session.add(new_form)
    db.session.commit()
    return jsonify({"message": "Form created successfully"}), 201
