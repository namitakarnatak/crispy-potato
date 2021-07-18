# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 04:12:24 2021

@author: a
"""
import requests 
from bs4 import BeautifulSoup

r=requests.get('https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen')

soup=BeautifulSoup(r.content,'lxml')
productlist=soup.find_all('div',class_='product-base')
productlist=[]
for item in productlist:
    print(item)
