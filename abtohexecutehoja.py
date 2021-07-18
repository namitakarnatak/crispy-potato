# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 07:07:42 2021

@author: a
"1=4444444444444
import requests

from bs4 import BeautifulSoup
import requests



url='https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen'
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
