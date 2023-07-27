from flask import jsonify
from marshmallow.exceptions import ValidationError


def handle_error(func):
    def wrapper(*args, **kwargs):
        # To handle all the exceptions
        try:
            return func(*args, **kwargs)
        except SyntaxError as e:
            return jsonify({"error": "Syntax Error: {}".format(e)}), 400
        except ValueError as e:
            return jsonify({"error": "Value Error: {}".format(e)}), 400
        except ValidationError as e:
            return jsonify({"error": "Validation error {}".format(e)}), 404
        except Exception as e:
            return jsonify({"error": "Internal Server Error: {}".format(e)}), 500

    return wrapper
