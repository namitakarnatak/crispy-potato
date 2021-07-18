# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:45:55 2021

@author: a
"""
import requests
from bs4 import BeautifulSoup
url="https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup)