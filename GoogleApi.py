import requests;
import os;
from dotenv import load_dotenv;
from bs4 import BeautifulSoup;

load_dotenv();

apiResponse = os.getenv("api_response_filepath");
googleApiUrl = "https://www.googleapis.com/customsearch/v1";
googleApiKey = os.getenv("google_api_key");


def APIRequest(query:str):
    params = {'key': googleApiKey, 'cx': 'YOUR_CSE_ID', 'q': {query}}
    response = requests.get(googleApiUrl, params=params);
    responseText = BeautifulSoup(response, 'html.parser').text;
    with open(apiResponse, "w", encoding="utf-8") as file:
        file.write(responseText);