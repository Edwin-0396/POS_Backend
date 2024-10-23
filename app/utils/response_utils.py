from flask import jsonify

class ResponseUtils:

    @staticmethod
    def success_response(message, data=None):
        response = {
            "status": "success",
            "message": message,
            "data": data
        }
        return jsonify(response), 200

    @staticmethod
    def error_response(message, status_code=400):
        response = {
            "status": "error",
            "message": message
        }
        return jsonify(response), status_code
