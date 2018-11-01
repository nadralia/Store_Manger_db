from flask import request, jsonify, Blueprint, make_response
from api.auth.decorator import response, response_message
from werkzeug.security import generate_password_hash, check_password_hash
from api.databases.functions import DatabaseFunctions
from api.controllers.user import UserController
from api.models.user import User
import datetime
import re
import jwt

auth = Blueprint('auth', __name__)

dbfuns = DatabaseFunctions()
user_controller = UserController()

@auth.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """
    User creates an account
    User sign up details are added to the database
    """
    if request.content_type != 'application/json':
        return response_message('Bad request', 'Content-type must be in json', 202) 

    data = request.get_json()

    try:
        if not data:
            return ({"Failed": "Empty request"}, 400)

        username = data['username']
        phone = data['phone']
        role  = data['role']
        password = generate_password_hash(data['password'])

        if not username:
            return response_message('Missing', 'Username required', 400)
        if not len(data['password']) > 4:
            return response_message('Failed', 'Ensure password is morethan 4 characters', 202)
        if not isinstance(username, str):
            return response_message('Type Error', 'username must all be string', 202)
        if not re.match("^[a-zA-Z0-9_.-]+$", username):
            return response_message('Space Error', 'Username should not have space, better user -', 400)
        if dbfuns.get_item_by_value('users', 'username', username):
            return response_message('Failed', 'User already registered', 409)
        user_added = dbfuns.create_a_new_user(username, phone, role, password)

        if user_added:
            return jsonify({
                        "message":
                        "User successfully added.", "User": user_controller.check_if_user_exists(username=username)
                    }), 201
        return jsonify({"message": "user not added"}), 400
    except KeyError as e:
        return ({'KeyError': str(e)})


@auth.route('/api/v1/auth/login', methods=['GET'])
def login():
    """User login if he supplies correct credentials
        token is generated and given to a user"""

    if request.content_type != 'application/json':
        return response_message('Bad request', 'Content-type must be in json', 202) 

    data = request.get_json()
    try:
        if not data:
            return ({"Failed": "Empty request"}, 400)

        username = data['username']
        password = generate_password_hash(data['password'])
        if not username and not password:
            return response_message('Failed', 'Username and password are required', 400)

        user = dbfuns.get_item_by_value('users', 'username', username)
        if not user:
            return response_message('Failed', 'incorect username', 401)
        new_user = User(user[0], user[1], user[2], user[3], user[4])
        if new_user.username == data['username'] and check_password_hash(
                    new_user.password, data['password']):
            payload = {
                'username': new_user.username,
                'exp': datetime.datetime.utcnow() +
                datetime.timedelta(days=60),
                'iat': datetime.datetime.utcnow(),
                'sub': new_user.user_id,
                'role': new_user.role
            }
            token = jwt.encode(
                payload,
                'mysecret',
                algorithm='HS256'
            )
            if token:
                return response(
                    new_user.user_id, new_user.username,
                    'You have succesfully logged in.',
                    token.decode('UTF-8'), 200)

        return response_message('Failed', 'incorrect password', 401)

    except KeyError as e:
        return ({'KeyError': str(e)})

@auth.route('/api/v1/users', methods=['GET'])
def fetch_users():
    """Fetches all the available users"""
    users = user_controller.get_all_users()

    if users:
        return jsonify({"users": users}), 200
    return jsonify({"message": "No users available"}), 404