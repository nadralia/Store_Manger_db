from flask import request, jsonify, Blueprint, make_response
from api.auth.decorator import response, response_message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from api.databases.functions import DatabaseFunctions
from api.validation import Validate
from api.controllers.user import UserController
from api.models.user import User
import datetime
import re
import jwt

auth = Blueprint('auth', __name__)

dbfuns = DatabaseFunctions()
user_controller = UserController()
validate = Validate()

@auth.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """
    User creates an account
    User sign up details are added to the database
    """
    data = request.get_json()
    search_keys = ("username","phone","role","password")
    if all(key in data.keys() for key in search_keys):
        username = data.get("username")
        phone = data.get("phone")
        role = data.get("role")
        password = data.get("password")

        invalid = validate.user_validation(username,role, password)
        if invalid:
            return jsonify({"message": invalid}), 400
        username_exists = user_controller.check_if_user_exists(username=username)
        if username_exists:
            return jsonify({"message": "username exists"}), 409
 
        new_user = user_controller.add_new_user(username=username,phone=phone, role=role, password=password)
        if new_user:
            return jsonify({"message": "User account created"}), 201
        else:
            return jsonify({"message": "User not created"}), 400
    return jsonify({"message": "Make sure you use the right keys"}), 400

@auth.route('/api/v1/auth/login', methods=['POST'])
def login():
    """User login if he supplies correct credentials
        token is generated and given to a user"""
    data = request.get_json()
    search_keys = ("username", "password")
    if all(key in data.keys() for key in search_keys):
        username = data.get("username")
        password = data.get("password")
        invalid = validate.login_validation(username, password)
        if invalid:
            return jsonify({"message": invalid}), 400

        user_token = {}
        expires = datetime.timedelta(days=1)
        grant_access = user_controller.login(username=username, password=password)
        if grant_access:
            access_token = create_access_token(identity= grant_access["username"], expires_delta=expires)
            user_token["logged in user"]=username
            user_token["token"] = access_token
            return jsonify(user_token), 200

        return jsonify({"message": "wrong login credentials or user does not exist"}), 400
    return jsonify({"message": "make sure you use the correct keys "}), 400

    
@auth.route('/api/v1/users', methods=['GET'])
def fetch_users():
    """Fetches all the available users"""
    users = user_controller.get_all_users()

    if users:
        return jsonify({"users": users}), 200
    return jsonify({"message": "No users available"}), 404