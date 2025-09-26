import psycopg2
import os
from dotenv import load_dotenv;
import psycopg2.extras
import json

load_dotenv();

dbname = os.getenv("AParser_pg_dbname");
user = os.getenv("AParser_pg_user");
password = os.getenv("AParser_pg_password");
host = os.getenv("AParser_pg_host");


def LoadResultToTable(table_name, params: dict):
    db_connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = db_connection.cursor()
    if cursor is None:
        print("Error: Unable to connect to the database.")
        return

    columns = ', '.join(params.keys())
    placeholders = ', '.join(['%s'] * len(params))
    values = tuple(
        psycopg2.extras.Json(v, dumps=lambda x: json.dumps(x, ensure_ascii=False))
        if isinstance(v, (dict, list)) else v
        for v in params.values()
    )

    sql:str = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    query = "INSERT INTO ggl_searchapi_answers (query, userid, answer) VALUES (%s, %s, %s)"
    cursor.execute(sql, values)

    print(f"Data inserted into {table_name} table successfully.")

    db_connection.commit()
    cursor.close()
    db_connection.close()