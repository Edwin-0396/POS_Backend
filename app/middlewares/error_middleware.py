from flask import jsonify
import logging

def error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Error: {str(e)}")
        return jsonify({"message": "An error occurred", "error": str(e)}), 500
