# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:45:55 2021

@author: a
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url= 'https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen'
uClient = uReq(my_url)

page_html= uClient.read()

uClient.close()
page_soup=soup(page_html,"html.parser")
print(page_soup.div)