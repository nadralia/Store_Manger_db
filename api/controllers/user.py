from api.databases.functions   import DatabaseFunctions
from api.models.user import User

# user controller class
class UserController:
    def __init__(self):
        self.dbfun = DatabaseFunctions()

    def check_if_user_exists(self, username):
        # check if username exists.
        user_exists = self.dbfun.check_if_username_exist(username=username)
        if user_exists:
            return user_exists
        return False

    def check_if_phone_exists(self, phone):
        # check if phone exists.
        phone_exists = self.dbfun.check_if_phonenumber_exist(phone=phone)
        if phone_exists:
            return True
        return False

    def user_login(self, username, password):
        # user login
        login = self.dbfun.login_a_user(username=username, password=password)
        if login:
            return login
        return False

    def get_user_role(self, role):
        # get current user's role
        role = self.dbfun.get_role_of_user(role=role)
        return role  

    def get_all_users(self):
        #function to fetch all the products
        user_list = self.dbfun.fetch_all_users()
        return user_list  
