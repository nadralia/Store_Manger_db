from api.models.sale import Sale
from api.databases.functions import DatabaseFunctions
from datetime import datetime


class SaleController:
    def __init__(self):
        self.dbfunctions = DatabaseFunctions()
        
    #function to add a new sale
    def create_a_sale(self, prod_id, prod_quantity, attendant, date_added):
        product = self.dbfunctions.fetch_a_single_product(prod_id=prod_id)
        if product:
            if product["prod_quantity"] > int(prod_quantity):
                prod_name = product["prod_name"]
                qty = int(prod_quantity)
                total_amount = (product["unit_price"]*int(prod_quantity))
                user = attendant
                date_added = datetime.now()
                sale = Sale(prod_id=prod_id, prod_name=prod_name, prod_quantity=qty,
                                total_amount=total_amount, attendant=user, date_added=date_added)
                self.dbfunctions.create_sale(prod_id=sale.prod_id,prod_name=sale.prod_name, prod_quantity=sale.prod_quantity,
                        total_amount=sale.unit_price, attendant=sale.attendant, date_created=sale.date_added)

                new_qty = int(product["prod_quantity"])- qty

                self.dbfunctions.update_product(prod_name=prod_name, prod_quantity=new_qty, 
                        unit_price=product["unit_price"], prod_id=prod_id, date_added=date_added)
                return True
            else:
                return False
        return False 

    def fetch_single_sale(self, sale_id):
        # fetch a sale record
        sale = self.dbfunctions.fetch_single_sale(sale_id=sale_id)
        return sale      

    def fetch_all_sales(self):
        #function to return all sales
        sales = self.dbfunctions.fetch_all_sales()
        return sales

    def fetch_single_sale_for_user(self, sale_id, username):
        #function to fetch a sale for a user
        sale = self.dbfunctions.get_a_sale_by_user(sale_id=sale_id, username=username)
        return sale  

    def fetch_all_sales_for_user(self, username):
        #function to fetch all sales for a user
        sales = self.dbfunctions.get_all_sales_by_user(username=username)
        return sales
    
   

 
