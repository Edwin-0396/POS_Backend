from flask import jsonify
from app.services.statistics_service import StatisticsService

class StatisticsController:

    def get_user_statistics(self, id_usuario):
        stats = StatisticsService.get_statistics_by_user(id_usuario)
        return jsonify(stats), 200

    def calculate_statistics(self, id_usuario):
        stats = StatisticsService.calculate_statistics(id_usuario)
        return jsonify({"message": "Statistics calculated", "statistics": stats}), 200
