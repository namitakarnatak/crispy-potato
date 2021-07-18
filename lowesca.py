# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:50:26 2021

@author: a
"""
import datetime
import time
from lxml import html
from bs4 import BeautifulSoup
import requests
import os
import sys
import undetected_chromedriver as uc

chrome_options = uc.ChromeOptions()
# chrome_options.add_argument("user-data-dir={}".format(user_dir))

chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', '--load-extension'])

# print('Opening')
driver = uc.Chrome(options=chrome_options)
driver.get('https://www.lowes.ca/product/pressure-washer-hoses/simpson-morflex-516-x-50-x-3700-psi-cold-water-replacementextension-hose-26019')






rating=driver.find_element_by_xpath("//div[@class='bv_avgRating_component_container notranslate']").text
print(rating)

review=driver.find_element_by_xpath("//div[@class='bv_numReviews_text']").text.strip('()')
print(review)



