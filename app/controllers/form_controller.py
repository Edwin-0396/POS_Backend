from flask import request, jsonify
from app.services.form_service import FormService

class FormController:

    def create_form(self):
        data = request.get_json()
        new_form = FormService.create_form(data)
        return jsonify({"message": "Form created successfully", "form": new_form}), 201

    def assign_form_to_route(self, id_formulario, id_ruta):
        result = FormService.assign_form_to_route(id_formulario, id_ruta)
        if result:
            return jsonify({"message": "Form assigned to route"}), 200
        return jsonify({"message": "Failed to assign form"}), 400
