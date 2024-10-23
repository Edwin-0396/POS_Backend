from flask import jsonify
from app.services.role_service import RoleService

class RoleController:

    def get_roles(self):
        roles = RoleService.get_all_roles()
        return jsonify(roles), 200

    def assign_role_to_user(self, id_usuario, id_rol):
        result = RoleService.assign_role_to_user(id_usuario, id_rol)
        if result:
            return jsonify({"message": "Role assigned successfully"}), 200
        return jsonify({"message": "Failed to assign role"}), 400
