from app.models.role import Role
from app.models.user import User
from app import db

class RoleService:

    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def assign_role_to_user(id_user, id_role):
        user = User.query.get(id_user)
        role = Role.query.get(id_role)
        if user and role:
            user.role = role.role_name
            db.session.commit()
            return user
        return None
