from app.models.form import Form
from app.models.route import Route
from app import db

class FormService:

    @staticmethod
    def create_form(data):
        new_form = Form(
            form_name=data['form_name'],
            creation_date=data['creation_date'],
            id_administrator=data['id_administrator'],
            fields=data['fields']
        )
        db.session.add(new_form)
        db.session.commit()
        return new_form

    @staticmethod
    def assign_form_to_route(id_formulario, id_route):
        form = Form.query.get(id_formulario)
        route = Route.query.get(id_route)
        if form and route:
            route.form = form
            db.session.commit()
            return route
        return None
