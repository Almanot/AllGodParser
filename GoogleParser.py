import requests
import bs4
import os
from dotenv import load_dotenv;

load_dotenv();

useragent = os.getenv("user_agent");
responseFilePath = os.getenv("response_filepath");
# Define the search query
query:str = input("Enter the search query: ").replace(' ', '+');
# Compose the Google search URL
url:str = "https://www.google.com/search?q={query}";

headers = {
    'User-Agent': useragent,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
response = requests.get(url, headers=headers);
with open(responseFilePath, "w", encoding="utf-8") as file:
    file.write(response.text);

def ParseSearchResults(response):
    results = bs4.BeautifulSoup(response, 'html.parser');
    sites = results.find_all('div', class_='g');