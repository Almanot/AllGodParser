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
    # In reason of big size data with unexpected structure and markups, loding is done in two steps, where answer loaded separately, to prevent errors.
    # first step creating a row with id, query and userid.
    rowdata: dict = {"query": query, "userid": 1};
    DBLoader.LoadResultToTable(rawanswer_tablename, rowdata);
    DBLoader.LoadResultToTable(rawanswer_tablename, {"answer": response.json()});