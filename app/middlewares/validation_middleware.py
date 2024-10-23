from functools import wraps
from flask import request, jsonify

def validate_request(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            errors = schema.validate(request.get_json())
            if errors:
                return jsonify({"message": "Validation failed", "errors": errors}), 400
            return f(*args, **kwargs)
        return decorated_function
    return decorator
