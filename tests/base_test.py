import unittest
from run import app
from flask import json
from api.databases.dbconnect import Database
from api.controllers.user import UserController

connection = Database()
user_controller = UserController()

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.username = "admin"
        self.phone = "0779-003145"
        self.role = "admin"
        self.password = "admin"
        self.app = app.test_client(self)
        connection.create_tables()
        self.register_admin()
        self.register_attendant()
        
    def tearDown(self):
        # Method to droP tables after the test is run
        connection.delete_tables()

    def register_admin(self):
        user_controller.add_new_user(self.username, self.phone, self.role, self.password)
        
    def register_attendant(self):
        user_controller.add_new_user("nadralia", "0779-003145", "attendant", "nadra2922")
    
    def admin_login(self):
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username=self.username, password=self.password))
        )
        reply = json.loads(response.data)
        return reply
    
    def attendant_login(self):
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="nadralia", password="nadra2922"))
        )
        reply = json.loads(response.data)
        return reply    