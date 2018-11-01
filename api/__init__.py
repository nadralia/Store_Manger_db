from flask import Flask 
from api.views.product import product
from api.views.user import auth
import os

app = Flask(__name__)

app.register_blueprint(product)

app.register_blueprint(auth)
#app.config.from_object(os.environ['ENVIRONMENT'])