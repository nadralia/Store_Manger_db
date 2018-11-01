from flask import Blueprint, jsonify, request, make_response
from api.controllers.product import ProductController
from api.models.product import Product
from api.validation import Validate
from datetime import datetime

from flask_jwt_extended import jwt_required, get_jwt_identity

product = Blueprint('product', __name__)

validate = Validate()
product_controller = ProductController()

@product.route('/api/v1/products', methods=['POST'])
@jwt_required
def add_product():
    """Creates a new product"""
    data = request.get_json()
    #require keys in the data input
    expected_keys = ("prod_name", "prod_quantity", "unit_price")
    if all(key in data.keys() for key in expected_keys):
        prod_name = data.get("prod_name")
        prod_quantity = data.get("prod_quantity")
        unit_price = data.get("unit_price")
        date_added = datetime.now()
        invalid = validate.product_validation(prod_name, prod_quantity, unit_price)
        if invalid:
            return jsonify({"message": invalid}), 400
        product_exists = product_controller.check_if_a_product_exist(prod_name=prod_name)
        if product_exists:
            #product exist but more quantity has to be added
            new_quantity = product_exists["prod_quantity"] + int(prod_quantity)
            product_controller.update_product(prod_name=prod_name,
                         prod_quantity=new_quantity, unit_price=unit_price, date_added=date_added, prod_id=product_exists["prod_id"])
            return jsonify({
            "message": "This product already exits, so its quantity has been updated", "Product":
                 product_controller.return_single_product(product_exists["prod_id"])}), 200

        product_added = product_controller.create_a_product(prod_name=prod_name, prod_quantity=int(
                    prod_quantity), unit_price=int(unit_price), date_added=date_added)
        if product_added:
            return jsonify({
                        "message":
                        "Product successfully added.", "Product": product_controller.check_if_a_product_exist(prod_name=prod_name)
                    }), 201
        return jsonify({"message": "product not added"}), 400
    return jsonify({"message": "a 'expected_keys' is missing in your request body"}), 400

@product.route('/api/v1/products', methods=['GET'])
def fetch_products():
    """Fetches all the available products"""
    products = product_controller.get_all_products()
    if products:
        return jsonify({"Products": products}), 200
    return jsonify({"message": "No products available"}), 404


@product.route('/api/v1/products/<int:prod_id>', methods=['GET'])
def fetch_single_product(prod_id):
    invalid = validate.validate_int_input_type(prod_id)
    if invalid:
        return jsonify({"message": invalid}), 400
    details = product_controller.return_single_product(prod_id=prod_id)
    if details:
        return jsonify({"Product": details}), 200
    return jsonify({"message": "Product not available"}), 404


@product.route('/api/v1/products/<int:prod_id>', methods=['DELETE'])
@jwt_required
def delete_product(prod_id):
    invalid = validate.validate_int_input_type(prod_id)
    if invalid:
        return jsonify({"message": invalid}), 400
    delete = product_controller.delete_product(prod_id=prod_id)
    if delete:
        return jsonify({"message": "product successfully deleted on safe mode"}), 200
    else:
        return jsonify({"message": "Product not deleted"}), 400

@product.route('/api/v1/products/<int:prod_id>', methods=['PUT'])
@jwt_required
def update_product(prod_id):
    invalid_id = validate.validate_int_input_type(prod_id)
    if invalid_id:
        return jsonify({"message": invalid_id}), 400
    data = request.get_json()
    search_keys = ("prod_name", "prod_quantity", "unit_price")
    if all(key in data.keys() for key in search_keys):
        prod_name = data.get("prod_name")
        prod_quantity = data.get("prod_quantity")
        unit_price = data.get("unit_price")
        date_added = datetime.now()

        invalid = validate.product_validation(prod_name, prod_quantity, unit_price)
        if invalid:
            return jsonify({"message": invalid}), 400
        update = product_controller.update_product(
            prod_name=prod_name, prod_quantity=prod_quantity, 
                unit_price=unit_price, prod_id=prod_id, date_added=date_added)
        if update:
            return jsonify({
            "message":
                "Product successfully updated.", "Product": product_controller.return_single_product(prod_id=prod_id)
            }), 200
        return jsonify({"message": "product not updated or doesn't exist"}), 400
    return jsonify({"message": "Make sure you use the right keys"}), 400