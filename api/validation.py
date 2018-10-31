from flask import jsonify, request
import re


class Validate:
    # add product validation.
    def product_validation(self, prod_name, prod_quantity, unit_price):
        if not prod_name:
            return "product name is missing"
        if prod_name == " ":
            return "product name is missing"
        if not re.match(r"^([a-zA-Z]+[-_\s])*[a-zA-Z]+$", prod_name):
            return "product name must have no white spaces"
        if not re.match(r"^[0-9]*$", prod_quantity):
            return "quantity must be only digits and must have no white spaces"
        if not re.match(r"^[0-9]*$", unit_price):
            return "price must be only digits and must have no white spaces"    
        if len(prod_name) < 4:
            return "product name should be more than 4 characters long"
        if not prod_quantity:
            return "quantity is missing"
        if prod_quantity == " ":
            return "quantity is missing"
        if int(prod_quantity) < 1:
            return "quantity should be at least 1 item"    
        if not unit_price:
            return "unit_price is missing"
        if int(unit_price) < 1:
            return "unit price should be greater than zero"    
        if unit_price == " ":
            return "unit_price is missing" 
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

    def validate_int_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Try inputting an interger"