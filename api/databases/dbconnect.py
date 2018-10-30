import psycopg2
from psycopg2.extras import RealDictCursor
import os
from api import app
from api.config import app_config

class Database():
    """class for app database"""

    def __init__(self):
        self.db = ''

        self.database_info = dict(
            dbname =self.db,
            user = 'postgre',
            password='nadra2922',
            host='localhost',
            port = 5432
        )

        """initialize db connection """
        try:
            if os.getenv('ENVIRONMENT') == "testing":
                db_conn = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="ayek",
                    dbname="store_db_test",
                ) 

                self.db_conn = db_conn
                self.c = self.db_conn.cursor()
                self.db_conn.autocommit = True
            elif os.getenv('ENVIRONMENT') == "development":
                db_conn = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="nadra2922",
                    dbname="store_db",
                ) 
                self.db_conn = db_conn
                self.c = self.db_conn.cursor()
                self.db_conn.autocommit = True
            else:
              db_conn = psycopg2.connect(
                host='',
                user='',
                password='',
                dbname="",
                port='5432'
              )
              self.db_conn = db_conn
              self.c = self.db_conn.cursor
              self.db_conn.autocommit = True
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)

    def create_tables(self):
        """ create tables """
        create_table = """CREATE TABLE IF NOT EXISTS users
        (user_id SERIAL PRIMARY KEY, username VARCHAR(30),
        email VARCHAR(100), location VARCHAR(100), password VARCHAR(150),
        role VARCHAR(100) DEFAULT 'user')"""

        create_table = """CREATE TABLE IF NOT EXISTS  products
        (prod_id SERIAL PRIMARY KEY, prod_name VARCHAR(38) NOT NULL UNIQUE,
        prod_quantity INTEGER NOT NULL, unit_price INTEGER NOT NULL,
        date_created TIMESTAMP DEFAULT NOW() )"""

        create_table =  """CREATE TABLE IF NOT EXISTS categories
        (category_id SERIAL PRIMARY KEY, category_name VARCHAR(56) UNIQUE NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()) """


