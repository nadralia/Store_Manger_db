from flask import Flask 
from api.views.product import product
from api.views.sales import sale
from api.views.user import auth
import os

app = Flask(__name__)

app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(auth)

app.config['JWT_SECRET_KEY'] = '\xa9\xc0w|\xae\rP\xa4\xbcg+\x9c"\xee{-\x14m\xb5\xd055j\x16'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)
