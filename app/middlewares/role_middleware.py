from flask import jsonify
from functools import wraps

def authorize(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user.rol not in allowed_roles:
                return jsonify({"message": "You do not have permission to access this resource!"}), 403
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator
