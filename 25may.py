# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:36:28 2021

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
driver.get('https://www.lowes.com/pd/SIMPSON-Aluminum-3600-PSI-2-5-GPM-Cold-Water-Gas-Pressure-Washer-with-Honda-Engine-CARB/1002703604')
reviews=driver.find_element_by_xpath("//div[@class='styles__RatingDiv-RC__sc-5hhhh2-2 keRFPo']").text

print(reviews)

# print(driver.find_element_by_id('main').text)

rating=driver.find_element_by_xpath("//div[@class='styles__RatingDiv-RC__sc-5hhhh2-2 keRFPo']").get_attribute('aria-label')
print(rating)


