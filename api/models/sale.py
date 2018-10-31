from api.models.product import Product

# Sale model class
class Sale(Product):
    def __init__(self,prod_name, prod_quantity,total_amount,attendant,date_added):
        super(Sale, self).__init__(prod_name, prod_quantity, total_amount, date_added)
        self.attendant = attendant
        self.date_added = date_added