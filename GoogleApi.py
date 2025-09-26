import requests;
import os;
from dotenv import load_dotenv;
from bs4 import BeautifulSoup;

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