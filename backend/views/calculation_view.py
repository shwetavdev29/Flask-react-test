from utils import handle_error
from flask.views import MethodView
from flask import request, jsonify
from schemas import SumNumbersSchema, ConcatenateStringsSchema


class SumView(MethodView):
    @staticmethod
    @handle_error
    def post():
        data = request.get_json()
        schema = SumNumbersSchema()
        validated_data = schema.load(data)
        numbers = validated_data.get("numbers", [])
        if not isinstance(numbers, list) or not all(
            isinstance(num, (int, float)) for num in numbers
        ):
            raise ValueError('Invalid input! "numbers" should be a list of numbers.')

        result = sum(numbers)
        return jsonify({"result": result})


class ConcatenateView(MethodView):
    @staticmethod
    @handle_error
    def post():
        data = request.get_json()
        schema = ConcatenateStringsSchema()
        validated_data = schema.load(data)
        string1 = validated_data.get("string1", "")
        string2 = validated_data.get("string2", "")
        result = string1 + string2
        return jsonify({"result": result})


class HomeView(MethodView):
    def get():
        return "App is working"
