# Register class-based views
from views.calculation_view import SumView, ConcatenateView, HomeView
from views.users_view import LoginView, RegisterView
from flask import Blueprint

# Create a Blueprint object
blueprint = Blueprint("api", __name__)
# Add the urls
blueprint.add_url_rule("/", view_func=HomeView, methods=["GET"])
blueprint.add_url_rule("/sum", view_func=SumView.as_view("sum"), methods=["POST"])
blueprint.add_url_rule(
    "/concatenate", view_func=ConcatenateView.as_view("concatenate"), methods=["POST"]
)

