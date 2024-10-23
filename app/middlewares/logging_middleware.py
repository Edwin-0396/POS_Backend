import logging
from flask import request

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = request.headers.get('Authorization', 'Anonymous')
        logging.info(f"Request Method: {request.method}, Request URL: {request.url}, User: {user}")
        return f(*args, **kwargs)
    return decorated_function
