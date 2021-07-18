import requests
from bs4 import BeautifulSoup

URL = 'https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

