import requests
from bs4 import BeautifulSoup
url="https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

