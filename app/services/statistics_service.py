from app.models.statistic import Statistic
from app.models.user import User
from app import db

class StatisticsService:

    @staticmethod
    def get_statistics_by_user(id_user):
        return Statistic.query.filter_by(id_user=id_user).first()

    @staticmethod
    def calculate_statistics(id_user):
        user = User.query.get(id_user)
        if user:
            total_routes = len(user.routes)
            average_checkin = sum([r.checkin_time for r in user.routes]) / total_routes if total_routes > 0 else 0
            average_checkout = sum([r.checkout_time for r in user.routes]) / total_routes if total_routes > 0 else 0

            new_stats = Statistic(
                id_user=id_user,
                total_routes_completed=total_routes,
                average_checkin_time=average_checkin,
                average_checkout_time=average_checkout,
                average_time_per_route=(average_checkout - average_checkin) if average_checkout else 0,
                completion_percentage=(total_routes / user.assigned_routes) * 100 if user.assigned_routes > 0 else 0
            )
            db.session.add(new_stats)
            db.session.commit()
            return new_stats
        return None
