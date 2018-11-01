from api.databases.dbconnect import Database

class DatabaseFunctions:
    def __init__(self):
        self.connect = Database()
        self.cursor = self.connect.dict_cursor

    """user helper functions begin it"""
    def create_a_new_user(self, username, phone, role, password):
        #function to create a new user
        query = (
            """INSERT INTO users (username, contact, role, password) VALUES ('{}', '{}', '{}', '{}')""".format(username, phone, role, password))
        self.cursor.execute(query)

    def check_if_username_exist(self,username):
        #function to check if username exists.
        query = ("""SELECT * FROM users where username = '{}'""".format(username))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return user
        return False    

    def check_if_phonenumber_exist(self,phone):
        # function to check if user phonenumber exists.
        query = ("""SELECT * FROM users where phone = '{}'""".format(phone))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return True
        return False 
    
    def get_role_of_user(self,role):
        #function to check if username exists.
        query = ("""SELECT * FROM users where role = '{}'""".format(role))
        self.cursor.execute(query)
        role =self.cursor.fetchone()
        if role:
            return role
        return False         

    def login_a_user(self, username, password):
        #function to login a user
        query = ("""SELECT * from users where username = '{}' and password='{}'""".format(username, password))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        return user
    
    """product helper functions begin it"""

    def insert_a_product(self, prod_name, prod_quantity, unit_price, date_added):
        #function to insert a product
        query = (
            """INSERT INTO products (prod_name, prod_quantity, unit_price, date_added) VALUES ('{}', '{}', '{}','{}')""".
            format(prod_name, prod_quantity, unit_price, date_added))
        self.cursor.execute(query)

    def check_if_product_exist_in_db(self,prod_name):
        #function to check if product exists.
        query = ("""SELECT * FROM products where prod_name = '{}'""".format(prod_name))
        self.cursor.execute(query)
        product = self.cursor.fetchone()
        if product:
            return product
        return False

    def update_product(self, prod_name, prod_quantity, unit_price, prod_id, date_added):
        #function to update product
        try:
            query = ("""UPDATE products SET prod_name = '{}', prod_quantity = '{}', unit_price = '{}', date_added = '{}' where prod_id = '{}'""" .format(
                prod_name, prod_quantity, unit_price, date_added, prod_id))
            self.cursor.execute(query)
            count = self.cursor.rowcount
            if int(count) > 0:
                return True
            else:
                return False   
        except:
            return False

    def fetch_a_single_product(self,prod_id):
        # function to get details of a product
        self.cursor.execute("SELECT * FROM products WHERE prod_id = '{}'" .format(prod_id))
        row = self.cursor.fetchone()
        return row

    def remove_product(self, prod_id):
        # function to remove a specific product
        query = ("""DELETE FROM products WHERE prod_id = '{}'""" .format(prod_id))
        self.cursor.execute(query)
        delete = self.cursor.rowcount
        if int(delete) > 0:
            return True
        else:
            return False   

    def fetch_all_products(self):
        """
        Query gets all that are recently available
        :admin
        """
        self.cursor.execute("SELECT * FROM products")
        all_products = self.cursor.fetchall()
        return all_products

    def create_sale(self, prod_id, prod_name, prod_quantity, total_amount, attendant, date_created):
        #function to create a sale 
        query = (
            """INSERT INTO sales (prod_id,prod_name, prod_quantity, total_amount, attendant, date_created) VALUES ('{}','{}', '{}', '{}', '{}', '{}')"""
            .format(prod_id, prod_name, prod_quantity, total_amount, attendant, date_created))
        self.cursor.execute(query)

    def fetch_single_sale(self, sale_id):
        #function to get the most recent sale record made
        self.cursor.execute("SELECT * FROM sales WHERE sale_id = '{}'" .format(sale_id))
        sale = self.cursor.fetchall()
        return sale

    def fetch_all_sales(self):
        #function to fetch all sales
        self.cursor.execute("SELECT * from sales")
        sales = self.cursor.fetchall()
        return sales

    def get_a_sale_by_user(self, sale_id, username):
        #function to get the most recent sale record made
        self.cursor.execute("SELECT * FROM sales WHERE sale_id = '{}' AND attendant = '{}'" .format(sale_id, username))
        sale = self.cursor.fetchall()
        return sale   

    def get_all_sales_by_user(self, username):
        #function to get all available sales
        self.cursor.execute("SELECT * FROM sales WHERE attendant = '{}'" .format(username))
        sales = self.cursor.fetchall()
        return sales

    def latest_sale(self):
        #function to get the most recent sale record made
        self.cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC LIMIT 1")
        sale = self.cursor.fetchall()
        return sale