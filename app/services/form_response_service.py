from app.models.form_response import FormResponse
from app import db

class FormResponseService:

    @staticmethod
    def submit_form_response(data):
        new_response = FormResponse(
            id_salesperson=data['id_salesperson'],
            id_route=data['id_route'],
            id_form=data['id_form'],
            responses=data['responses'],
            photo=data.get('photo'),
            geolocation=data['geolocation'],
            checkin_datetime=data['checkin_datetime'],
            checkout_datetime=data['checkout_datetime']
        )
        db.session.add(new_response)
        db.session.commit()
        return new_response

    @staticmethod
    def get_responses_by_route(id_route):
        return FormResponse.query.filter_by(id_route=id_route).all()
