from api import app
from flask import jsonify
from api.databases.dbconnect import Database

import os

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'message': "Missing Authorization Header"}),401

@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': "Requested URL is invalid"}),405

@app.errorhandler(404)
def content_not_found(error):
    return jsonify({'message': "Requested url is not found"}),404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': "Internal server error"}),500

if __name__ == "__main__":
    db_connection = Database()
    db_connection.create_tables()
    app.run(debug=True)