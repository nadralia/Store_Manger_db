from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestProducts(BaseTestCase):

    def test_adding_product_successfully(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(prod_name="Jackets", prod_quantity="20",unit_price="200"),)   
                             ) 
        reply = json.loads(response.data.decode())
        self.assertIn(("Jackets"), reply.get("Product").values())
        self.assertEqual(response.status_code, 201)

    def test_adding_product_existing_product(self):
        admin_login= self.admin_login()
        response = self.app.post("/api/v1/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(prod_name="Jackets", prod_quantity="20",unit_price="200"),)   
                             )
        response = self.app.post("/api/v1/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
                                 data=json.dumps(dict(prod_name="Jackets", prod_quantity="20",unit_price="200"),)   
                             )                      
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "This product already exits, so its quantity has been updated")
        self.assertEqual(response.status_code, 200)

 