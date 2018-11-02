from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class Test_auth(BaseTestCase):

    def test_registration_success(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="adralia", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "User account created")
        self.assertEqual(response.status_code, 201)

    def test_registration_with_short_username(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nad", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username should be more than 4 characters long")
        self.assertEqual(response.status_code, 400)  

    def test_registration_with_missing_keys(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict( phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "Make sure you use the right keys")
        self.assertEqual(response.status_code, 400)   

    def test_registration_with_wrong_username(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )                       
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "usename is missing")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_no_username(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username=" ", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )                       
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)    

    def test_registration_with_existing_username(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nadralia2", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )
        response2 = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nadralia2", phone="0700-000000", role="attendant", password="nadra2922"),)
                                 )                         
        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "username exists")
        self.assertEqual(response2.status_code, 409)

    def test_registration_with_wrong_role(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nadralia2", phone="0700-000000", role="attend", password="nadra2922"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "role should either be admin or attendant")
        self.assertEqual(response.status_code, 400) 

    def test_registration_with_impromper_username(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nadralia 2", phone="0700-000000", role="admin", password="nadra2922"),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username must have no white spaces")
        self.assertEqual(response.status_code, 400)
    
    def test_registration_with_no_password(self):
        """ Test for successful user signup """
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(username="nadral2", phone="0700-000000", role="admin", password=""),)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "password is missing")
        self.assertEqual(response.status_code, 400)    

    def test_user_login_successful(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="nadralia", password="nadra2922"))
        )
        self.assertEqual(response.status_code, 200)

    def test_user_login_unsuccessful(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="nadral", password="nadral"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "wrong login credentials or user does not exist")
        self.assertEqual(response.status_code, 400)
        
    def test_user_login_with_wrong_username(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username=" nadral", password="nadral"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "wrong login credentials or user does not exist")
        self.assertEqual(response.status_code, 400)

    def test_user_login_with_wrong_username_2(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="", password="nadral"))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)

    def test_user_login_with_no_password(self):
        """ Test for successful login """
        self.register_attendant()
        response = self.app.post(
            "/api/v1/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="nadralia", password=""))
        )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "password is missing")
        self.assertEqual(response.status_code, 400)                     
      
