import os
from werkzeug.utils import secure_filename
from flask import current_app

class FileUtils:

    @staticmethod
    def allowed_file(filename):
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @staticmethod
    def save_file(file, folder='uploads'):
        if file and FileUtils.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], folder, filename)
            file.save(filepath)
            return filepath
        return None
