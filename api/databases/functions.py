from api.databases.dbconnect import Database

class DatabaseFunctions:
    def __init__(self):
        self.connect = Database()
        self.cursor = self.connect.dict_cursor

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
    
