from flask import jsonify


def error_response(message, code):
    return jsonify({'error': message}), code
