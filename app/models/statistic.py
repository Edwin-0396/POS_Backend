from app import db

class Statistic(db.Model):
    __tablename__ = 'statistic'

    id_statistic = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)

    total_routes_completed = db.Column(db.Integer, nullable=False, default=0)
    average_checkin_time = db.Column(db.Float, nullable=False, default=0.0)
    average_checkout_time = db.Column(db.Float, nullable=False, default=0.0)
    average_time_per_route = db.Column(db.Float, nullable=False, default=0.0)
    completion_percentage = db.Column(db.Float, nullable=False, default=0.0)

    user = relationship('User', back_populates='statistics')

    def __repr__(self):
        return f'<Statistic {self.id_statistic}>'
