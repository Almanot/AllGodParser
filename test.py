import os
import psycopg2
from dotenv import load_dotenv;
load_dotenv();

dbname = os.getenv("AParser_pg_dbname");
user = os.getenv("AParser_pg_user");
password = os.getenv("AParser_pg_password");
host = os.getenv("AParser_pg_host");

db_connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = db_connection.cursor()
if cursor is None:
    print("Error: Unable to connect to the database.")

print("Data inserted into table successfully.")
db_connection.commit()
cursor.close()
db_connection.close()