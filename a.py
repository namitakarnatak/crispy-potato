from bs4 import BeautifulSoup
import requests 
r=requests.get('https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen')
soup=BeautifulSoup(r.content,'lxml')
title=soup.find_all("h3",{"class": "product-brand"})
price=soup.find_all("h4",{"class": "product-price"})
images=soup.find_all("div",{"class":"product-imageSliderContainer"})
for title,price  in zip(title,price):
	print ("title: " ,title)
	print ("price:" ,price)
