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

    # Loading raw anwser to DB
    rowdata: dict = {"query": query, "userid": 1, "answer":response.json()};
    DBLoader.LoadResultToTable(rawanswer_tablename, rowdata);

if __name__ == "__main__":
    query = input("Enter the search query: ");
    NewSearch(query);