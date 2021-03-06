from flask import Flask 
from api.views.product import product
from api.views.sales import sale
from api.views.user import auth
import os

app = Flask(__name__)

app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(auth)

app.config['JWT_SECRET_KEY'] = 'sec-def-oscar-zulu-3-zero-niner'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)