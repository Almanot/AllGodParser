import DBLoader
import GoogleApi

def NewSearch(query):
    response = GoogleApi.SearchAPIRequest(query, lang="uk", num=10);
    DBLoader.LoadResultToDB(response.json());