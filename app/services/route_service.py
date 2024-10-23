from app.models.route import Route
from app.models.user import User
from app import db

class RouteService:

    @staticmethod
    def create_route(data):
        new_route = Route(
            route_name=data['route_name'],
            creation_date=data['creation_date'],
            id_administrator=data['id_administrator']
        )
        db.session.add(new_route)
        db.session.commit()
        return new_route

    @staticmethod
    def assign_vendedora(id_route, id_vendedora):
        route = Route.query.get(id_route)
        vendedora = User.query.get(id_vendedora)
        if route and vendedora:
            route.salesperson = vendedora
            db.session.commit()
            return route
        return None

    @staticmethod
    def record_checkin(id_route, checkin_data):
        route = Route.query.get(id_route)
        if route:
            route.checkin_history = checkin_data
            db.session.commit()
            return route
        return None

    @staticmethod
    def record_checkout(id_route, checkout_data):
        route = Route.query.get(id_route)
        if route:
            route.checkout_history = checkout_data
            db.session.commit()
            return route
        return None
