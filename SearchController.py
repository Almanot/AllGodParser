import DBLoader;
import GoogleApi;
import Data;
from dotenv import load_dotenv;
import os;
import json;

load_dotenv();

rawanswer_tablename = os.getenv("AParser_pg_table_name");
parsedAnswer_tablename = os.getenv("AParser_pg_table_name");

def NewSearch(query):
    response = GoogleApi.SearchAPIRequest(query, lang="uk", num=10);
    DBLoader.LoadResultToDB(response.json());

if __name__ == "__main__":
    query = input("Enter search query: ");
    NewSearch(query);