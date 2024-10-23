from flask import request, jsonify
from app.services.form_response_service import FormResponseService

class FormResponseController:

    def submit_form_response(self):
        data = request.get_json()
        response = FormResponseService.submit_form_response(data)
        return jsonify({"message": "Form response submitted", "response": response}), 201

    def get_form_responses_by_route(self, id_ruta):
        responses = FormResponseService.get_responses_by_route(id_ruta)
        return jsonify(responses), 200
