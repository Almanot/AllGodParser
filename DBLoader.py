import psycopg2
import os
from dotenv import load_dotenv;

load_dotenv();

dbname = os.getenv("AParser_pg_dbname");
user = os.getenv("AParser_pg_user");
password = os.getenv("AParser_pg_password");
table_name = os.getenv("AParser_pg_table_name");
host = "localhost";


def LoadResultToTable(table_name, params: dict):
    db_connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = db_connection.cursor()

    columns = ', '.join(params.keys())
    placeholders = ', '.join(['%s'] * len(params))
    values = tuple(params.values())

    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, values)

    db_connection.commit()
    cursor.close()
    db_connection.close()