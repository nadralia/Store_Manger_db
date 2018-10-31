from api.models.product import Product
from api.databases.functions import DatabaseFunctions


class ProductController:
    def __init__(self):
        self.dbfunctions = DatabaseFunctions()

    def create_a_product(self, prod_name, prod_quantity, unit_price):
        #function to create a new product
        new_product = Product(prod_name=prod_name,
                              prod_quantity=prod_quantity, unit_price=unit_price)
        self.dbfunctions.insert_a_product(prod_name=new_product.prod_name,
                                   prod_quantity=new_product.prod_quantity, unit_price=new_product.unit_price)
        return True

    def check_if_a_product_exist(self, prod_name):
        #function to check if a product exists.
        product_exists = self.dbfunctions.check_if_product_exist_in_db(prod_name=prod_name)
        if product_exists:
            return product_exists
        return False

    def update_product(self, prod_name, prod_quantity, unit_price, prod_id):
        #function to update a product
        update = self.dbfunctions.update_product(
            prod_name=prod_name, prod_quantity=prod_quantity, unit_price=unit_price, prod_id=prod_id)
        if update:
            return True
        else:
            return False

    def return_single_product(self, prod_id):
        #function to return a single product
        product = self.dbfunctions.fetch_a_single_product(prod_id=prod_id)
        if product:
            return product
        return False

    def delete_product(self, prod_id):
        #function to delete a single product using product id
        delete_item = self.dbfunctions.remove_product(prod_id=prod_id)
        if delete_item:
            return True
        return False
