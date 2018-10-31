from api import app
from api.databases.dbconnect import Database

import os

print(os.environ['ENVIRONMENT'])

if __name__ == "__main__":
    db_connection = Database()
    db_connection.create_tables()
    app.run(debug=True)