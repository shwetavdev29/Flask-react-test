# Backend
```
Python Flask Backend - Question 1:

Create a simple Flask API with two endpoints. The first endpoint should accept a JSON object containing a list of numbers and return the sum of the numbers. The second endpoint should accept a JSON object containing two strings and return the concatenated result. Demonstrate error handling for invalid input.

Explanation:
(I added the calculation_view for the above task one for adding the numbers in which used the marshmallow for validations. Marshmallow allows us to define a schema for the data that the API expects in the request body. By defining a schema, we can enforce rules on the data, such as required fields, data types, and validation functions. If the request data does not match the schema, Marshmallow will raise validation errors, which can be caught and handled in a standardized way and it allow use for many purpose. I also used the decorator that is the handle_error  for handling each type of exceptions.)


Python Flask Backend - Question 2:

Implement a simple user authentication system using Flask. Create an endpoint for user registration that accepts a username and password, stores them in a dictionary (as a stand-in for a real database), and returns a success message. Then create an endpoint for user login that checks if the provided username and password match the stored values, and if so, returns an "access granted" message; otherwise, return an "access denied" message.

Explanation:
( I added users_view for both sub two tasks for registration and another for login )
```

## Installation

1. Make sure you have Python 3.8 installed.

2. Clone this repository


# Dependencies
```
blinker==1.6.2
click==8.1.6
Flask==2.3.2
importlib-metadata==6.8.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
marshmallow==3.20.1
packaging==23.1
Werkzeug==2.3.6
zipp==3.16.2
```

## Command

`python app.py`

`The backend will now be running at http://127.0.0.1:5000.`




