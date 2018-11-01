import psycopg2
from psycopg2 import extras as _extra
from psycopg2.extensions import cursor as _cursor

class Database():
    """class for app database"""

    def __init__(self):
        self.db_con = psycopg2.connect(
            database="store_db", user="postgres", password="nadra2922", host="localhost", port="5432")
        self.db_con.autocommit = True
        self.dict_cursor = self.db_con.cursor(cursor_factory=_extra.RealDictCursor)

    def create_tables(self):
        create_tables = (
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                phone VARCHAR(50) NOT NULL,
                role VARCHAR(10) NOT NULL,
                password VARCHAR(150) NOT NULL
            )
            """,

            """
			CREATE TABLE IF NOT EXISTS products (
				prod_id SERIAL PRIMARY KEY,
				prod_name VARCHAR(50) NOT NULL,
				prod_quantity INTEGER NOT NULL,
				unit_price INTEGER NOT NULL,
                date_added timestamp NOT NULL	
			)
			""",
            """
            CREATE TABLE IF NOT EXISTS categories(
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR(56) UNIQUE NOT NULL,
                created_at timestamp DEFAULT NOW()
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS sales (
                 sale_id SERIAL PRIMARY KEY,
                 prod_name VARCHAR(50) NOT NULL,
                 prod_quantity INTEGER NOT NULL,
                 total_amount INTEGER NOT NULL,
                 attendant VARCHAR(50) NOT NULL,
                 date_created timestamp NOT NULL
             )
             """
        )
        for table in create_tables:
            self.dict_cursor.execute(table)

    def delete_tables(self):

        delete_tables = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,

            """
			DROP TABLE IF EXISTS products CASCADE
						""",

            """
            DROP TABLE IF EXISTS sales CASCADE
            """
        )
        for tables in delete_tables:
            self.dict_cursor.execute(tables)

