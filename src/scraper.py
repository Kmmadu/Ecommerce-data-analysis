from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_Internet_companies'

responce = requests.get(url)

soup = BeautifulSoup(responce.text, 'html')