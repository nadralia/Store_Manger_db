from flask import Flask 

app = Flask(__name__)

#testing an endpoint
@app.route('/')
def hello():
    return "Hello World!"