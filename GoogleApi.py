import requests;
import os;
from dotenv import load_dotenv;
from bs4 import BeautifulSoup;
from unittest.mock import Mock;
import json;

load_dotenv();

googleApiUrl = "https://www.googleapis.com/customsearch/v1";
googleApiKey = os.getenv("google_api_key");
searchEngineID = os.getenv("search_engine_id");


def SearchAPIRequest(query:str, **params):
    print(f"Searching for '{query}'");
    base_params = {
        'key': googleApiKey,
        'cx': searchEngineID,
        'q': query
    }
    base_params.update(params)
    response = requests.get(googleApiUrl, params=base_params);
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}");
    return response;

# mock version
def SearchAPIRequest(query:str, **params):
    # mock
    mockresponse = Mock();
    with open("query_Швабра купить Днепр.json", "r", encoding="utf-8") as file:
        mockresponse.json.return_value = json.load(file);
    return mockresponse;