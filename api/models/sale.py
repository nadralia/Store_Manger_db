from api.models.product import Product

# Sale model class
class Sale(Product):
    def __init__(self,prod_id, prod_name, prod_quantity,total_amount,date_added, attendant):
        super(Sale, self).__init__(prod_name, prod_quantity, total_amount, date_added)
        self.attendant = attendant
        self.prod_id   = prod_id
