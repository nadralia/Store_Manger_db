from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.controllers.sale import SaleController
from api.controllers.user import UserController
from api.databases.functions import DatabaseFunctions
from api.models.sale import Sale
from api.validation import Validate
from datetime import datetime

validate = Validate()
dbfunctions = DatabaseFunctions()
sale_controller = SaleController()
user_controller = UserController()

sale = Blueprint('sale', __name__) 

@sale.route('/api/v1/sales/<int:prod_id>', methods=['POST'])
def create_sale_record(prod_id):
    data = request.get_json()
    if "prod_quantity" in data.keys():
        qty = data.get("prod_quantity")
        date = datetime.now()
        attendant = get_jwt_identity()
        invalid_quantity = validate.validate_int_input_type(qty)
        if invalid_quantity:
            return jsonify({"message": invalid_quantity}), 400
        invalid_id = validate.validate_int_input_type(prod_id)
        
        if invalid_id:
            return jsonify({"message": invalid_id}), 400
        sale = sale_controller.create_a_sale(
            prod_id=prod_id, prod_quantity=qty, attendant=attendant, date_added=date)
        if sale:
            return jsonify({"message": "sale successfully added", "sales": dbfunctions.latest_sale()}), 201
        else:
            return jsonify({"message": "sale not added. Product does not exist "}), 400

@sale.route('/api/v1/sales', methods=['GET'])
def fetch_sale_orders():
    """This endpoint fetches all sale records"""
    #user = get_jwt_identity()
    #role = user_controller.get_user_role(role=user)
    #if role["role"] == 'admin':
    sales = sale_controller.fetch_all_sales()
    #elif role["role"] == 'attendant':
    #   sales = sale_controller.fetch_all_sales_for_user(username=user)
    if sales:
        return jsonify({"Sales": sales}), 200
    return jsonify({"message": "no sales recorded yet"}), 404   

@sale.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_single_record(sale_id):
    invalid = validate.validate_int_input_type(sale_id)
    if invalid:
        return jsonify({"message": invalid}), 400
    #user = get_jwt_identity()
    
    #role = user_controller.get_user_role(role=user)
    #if role["role"] == 'admin':    
    sale = sale_controller.fetch_single_sale(sale_id=sale_id)
    #elif role["role"] == 'attendant':
       # sale = sale_controller.fetch_single_sale_for_user(sale_id=sale_id, username=user)
    if sale:
        return jsonify({"Sale details": sale}), 200
    return jsonify({"message": "sale record not added yet"}), 404

    
