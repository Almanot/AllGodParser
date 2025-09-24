import psycopg2
import os
from dotenv import load_dotenv;

load_dotenv();

dbname = os.getenv("AParser_pg_dbname");
user = os.getenv("AParser_pg_user");
password = os.getenv("AParser_pg_password");
host = "localhost";

def LoadToResultDB(result_data):
    db_connection = psycopg2.connect(dbname,user,password,host)
    cursor = db_connection.cursor()
    
    cursor.execute(result_data)

    db_connection.commit()
    cursor.close()
    db_connection.close()