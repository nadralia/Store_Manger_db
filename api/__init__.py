from flask import Flask 
from api.views.product import product
import os

app = Flask(__name__)

app.register_blueprint(product)

#app.config.from_object(os.environ['ENVIRONMENT'])