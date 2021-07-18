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

driver = uc.Chrome(options=chrome_options)


def lowes_com_review_rating(url):
    driver.get(url)

    rating = driver.find_element_by_xpath("//div[@class='styles__RatingDiv-RC__sc-5hhhh2-2 keRFPo']").get_attribute(
        'aria-label').strip()
    rating_stars = rating.split(' ')[0]
    review_count = rating.split(' ')[-2]

    return rating_stars,review_count


def lowes_ca_review_rating(url):
    driver.get(url)

    rating_stars = driver.find_element_by_xpath("//div[@class='bv_avgRating_component_container notranslate']").text
    
    review_count=driver.find_element_by_xpath("//div[@class='bv_numReviews_text']").text.strip('()')
    
    return rating_stars,review_count


def lowes_review_rating_tra(url):
    driver.get(url)
    rating_stars=driver.find_element_by_xpath("/html/body/div[15]/div[3]/div[1]/div[2]/div[1]/div[1]/a/span[3]").text.strip('()')
    review_count=driver.find_element_by_xpath("/html/body/div[15]/div[3]/div[1]/div[2]/div[1]/div[1]/a/span[2]").text
    
    return rating_stars,review_count


    
    


# if __name__ == '__main__':
lowes_rating_stars,lowes_review_count=lowes_com_review_rating('https://www.lowes.com/pd/SIMPSON-Aluminum-3600-PSI-2-5-GPM-Cold-Water-Gas-Pressure-Washer-with-Honda-Engine-CARB/1002703604')
print(lowes_rating_stars,lowes_review_count)

lowes_ca_rating_stars,lowes_ca_review_count=lowes_ca_review_rating('https://www.lowes.ca/product/joist-hangers/simpson-strong-tie-double-shear-hanger-z-max-108806')
print(lowes_ca_rating_stars,lowes_ca_review_count)

lowes_tra_rating_stars,lowes_tra_review_count=lowes_review_rating_tra('https://www.tractorsupply.com/tsc/product/simpson-powershot-series-ps60869-4000-psi-@-35-gpm-gas-pressure-washer-powered-by-honda')
print(lowes_tra_rating_stars,lowes_tra_review_count)