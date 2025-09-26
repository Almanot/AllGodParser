import DBLoader;
import GoogleApi;
import Data;
from dotenv import load_dotenv;
import os;

load_dotenv();

rawanswer_tablename = os.getenv("AParser_pg_raw_table_name");
parsedAnswer_tablename = os.getenv("AParser_pg_table_name");

def NewSearch(query, userid='1'):
    response = GoogleApi.SearchAPIRequest(query, lang="uk", num=10);
    loadingdata: dict = {"query": query, "userid": userid, "answer": response.json()};
    DBLoader.LoadResultToTable(rawanswer_tablename, loadingdata);

if __name__ == "__main__":
    # this is hack to support cyrillic input in Windows console
    query = input("Enter search query: ").encode('utf-8', "ignore").decode('utf-8');
    NewSearch(query);