from app import db
from sqlalchemy.orm import relationship

class Role(db.Model):
    __tablename__ = 'role'

    id_role = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)

    users = relationship('User', back_populates='role')

    def __repr__(self):
        return f'<Role {self.role_name}>'
