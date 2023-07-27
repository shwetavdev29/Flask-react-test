from flask import Flask, jsonify, request
from flask.views import MethodView

# A dictionary to store user credentials (stand-in for a real database)
users = {}


class RegisterView(MethodView):
    def post(self):
        # Get the JSON data from the request body
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Check if username and password are provided
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if the username already exists
        if username in users:
            return (
                jsonify(
                    {"error": "Username already exists. Please choose a different one."}
                ),
                400,
            )

        # Store the username and password in the users dictionary
        users[username] = password

        # Return a success message
        return jsonify({"message": "User registered successfully."}), 201


class LoginView(MethodView):
    def post(self):
        # Get the JSON data from the request body
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Check if username and password are provided
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if the provided username exists in the users dictionary
        # and if the provided password matches the stored password
        if username not in users or users[username] != password:
            return jsonify({"error": "Invalid username or password."}), 401

        # Return an "access granted" message with the username
        return (
            jsonify({"message": "Access granted. Welcome, {}!".format(username)}),
            200,
        )
