from flask import request, jsonify
from app.services.route_service import RouteService

class RouteController:

    def create_route(self):
        data = request.get_json()
        new_route = RouteService.create_route(data)
        return jsonify({"message": "Route created successfully", "route": new_route}), 201

    def assign_vendedora_to_route(self, id_ruta, id_vendedora):
        result = RouteService.assign_vendedora(id_ruta, id_vendedora)
        if result:
            return jsonify({"message": "Vendedora assigned to route"}), 200
        return jsonify({"message": "Failed to assign vendedora"}), 400

    def record_checkin(self, id_ruta, checkin_data):
        updated_route = RouteService.record_checkin(id_ruta, checkin_data)
        return jsonify({"message": "Checkin recorded", "route": updated_route}), 200

    def record_checkout(self, id_ruta, checkout_data):
        updated_route = RouteService.record_checkout(id_ruta, checkout_data)
        return jsonify({"message": "Checkout recorded", "route": updated_route}), 200
