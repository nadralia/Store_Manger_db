#product model class
class Product:
    def __init__(self, prod_name, prod_quantity, unit_price, date_added):
        self.prod_name = prod_name
        self.prod_quantity = prod_quantity
        self.unit_price = unit_price
        self.date_added = date_added