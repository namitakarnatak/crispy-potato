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
driver.get('https://www.homedepot.com/p/Simpson-MegaShot-MSH3125-S-3200-PSI-at-2-5-GPM-HONDA-GC190-Cold-Water-Pressure-Washer-49-State-60551/203177499')
reviews=driver.find_element_by_xpath("//span[@class='product-details__review-count']").text.strip('()')

print(reviews)

rating=BeautifulSoup.find_all('span',{'class':'ratings-and-reviews-overview__desktop__list__review-average'}).text

print(rating)


