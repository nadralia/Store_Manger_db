from flask import jsonify, request
import re


class Validate:
    # add user validation
    def user_validation(self, data):
        # Validates user fields
        try:
            if len(data.keys()) == 0:
                return "No user added", 400
            if data['username'] == "":
                return "User name cannot be blank", 400
            if data['password'] == "":
                return "Password cannot be blank", 400
            if not re.match(r"([a-zA-Z0-9])", data['username']):
                return "Only alphanumerics allowed in user name", 400
            if re.match(r"([0-9])", data['username']):
                return "user name cannot contain numbers only", 400
            if len(data['password']) < 5:
                return "Password too short", 400
            else:
                return "is_valid"
        except KeyError:
            return "Invalid"