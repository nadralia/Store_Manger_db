#product model class
class Product:
    def __init__(self, prod_name, prod_quantity, unit_price):
        self.prod_name = prod_name
        self.prod_quantity = prod_quantity
        self.unit_price = unit_price