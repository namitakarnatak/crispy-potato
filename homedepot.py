# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:03:50 2021

@author: a
"""
import datetime
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
driver.get('https://www.homedepot.ca/product/1001538760')






review=driver.find_element_by_xpath("//span[@class='acl-rating__reviews']").text.strip('()')

print(review)

rating=driver.find_element_by_xpath("/html/body/app-container/div[1]/landing/div[2]/main/section/dl/div/acl-accordion-panel/div[2]/div/div/product-reviews-wrapper-component/div[2]/div/div[2]/div[1]/div/button/div[2]").get_attribute('aria-label').strip()
# rating=driver.find_element_by_xpath("//div[@id='ratings-summary']/div[2]")
# rating=driver.find_element_by_xpath("//div[@class='bv_avgRating_component_container notranslate']").text
# rating_count=rating.split('')[3]
print(rating)



