# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:14:50 2021

@author: a
"""
import argparse
import csv
import datetime
import hashlib
import sys
import time
import numpy as np

import requests
import logging
import os

import pandas as pd
from bs4 import BeautifulSoup
from azure.cosmosdb.table.tableservice import TableService, TableBatch
from azure.storage.blob import BlockBlobService
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from azure.cosmosdb.table.tableservice import TableService
from email.mime.text import MIMEText
import smtplib
import undetected_chromedriver as uc

# Azure Storage account name and primary key
ACCOUNT_NAME = 'bvtablescopy'
ACCOUNT_KEY = 'KUCxlPH2Ndxcen764gFctcczeqNkwK91bR7Q2lfpnHGQx2AJKqPJAshYFqM/prD4gfuPBxf6uto0s6Ava3gb1A=='

path = 'C://chromedriver.exe'
uc.install(executable_path=path)
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', '--load-extension'])
# driver = webdriver.Chrome(options=chrome_options, executable_path=path)
# driver.implicitly_wait(2)


error_email = ''
is_popup_model_present = True

email_string = ''


# def login_costco():
#     global driver, error_email, is_popup_model_present, ca_scrap
#     if not ca_scrap:
#         driver.get('https://www.costco.com/LogonForm')
#         passw = 't3v@4#5CErU'
#     else:
#         driver.get('https://www.costco.ca/LogonForm')
#         passw = '7p@Dy5Dd&9E'
#
#     time.sleep(3.3)
#
#     try:
#         if is_popup_model_present:
#             driver.find_element_by_xpath('//*[@id="region-radio-buttons"]//input[@value="ON"]').click()
#             driver.find_element_by_id('language-region-set').click()
#             is_popup_model_present = False
#     except:
#         pass
#
#     try:
#         driver.find_element_by_id('postal-code-continue').click()
#     except:
#         pass
#
#     try:
#         driver.find_element_by_id('logonId').send_keys('podea@pjboren.com')
#         time.sleep(.3)
#         driver.find_element_by_id('logonPassword').send_keys(passw)
#         time.sleep(.2)
#     except:
#         error_email += 'Error in login function.'
#
#     try:
#         for sign_in_button in driver.find_elements_by_tag_name('input'):
#             try:
#                 if sign_in_button.get_attribute('value') == 'Sign In':
#                     sign_in_button.click()
#                     time.sleep(2.1)
#                     break
#             except:
#                 pass
#     except:
#         error_email += 'Error in login function, Clicking on button.'
#

def main(logger, weekly_category_scrap, partition_key, search_term, ca_scrap):
    global error_email, is_popup_model_present, email_string
    table_service = TableService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

    if ca_scrap:
        costco_product_table = 'CAcostcoProducts'
        costco_category_product_table = 'CAcostcoCategoryProducts'
    else:
        costco_product_table = 'costcoProducts'
        costco_category_product_table = 'costcoCategoryProducts'

    # insertion_table = 'CostcoTest'
    # if not table_service.exists(insertion_table):
    #     table_service.create_table(insertion_table)

    insertion_table = 'CostcoagainTest'
    if not table_service.exists(insertion_table):
        table_service.create_table(insertion_table)

    # logger.info('Reading XLSX file.')
    #
    # df = pd.read_excel('Ove_Program_Sheet_-_Model_-_Description.xlsx')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    # logger.info('itrating over dataframe created using XLSX file.')
    # this search term is for what ?
    if ca_scrap:
        if search_term == 'OVE':
            search_term = 'OV'

    # partition_key = 'OVE'
    if not ca_scrap:
        main_url_prod = 'https://www.costco.com/CatalogSearch?dept=All&keyword={}'.format(search_term.replace('-', ''))
    else:
        main_url_prod = 'https://www.costco.ca/CatalogSearch?dept=All&keyword={}'.format(search_term.replace('-', ''))

    logger.info(
        'Trying to get all products from Costco for brand `{}` keyword: `{}`'.format(partition_key, search_term))

    logger.info('Going to search URL for getting all products `{}`'.format(main_url_prod))
    category_response_ = requests.get(main_url_prod, headers=headers)
    html_category_ = category_response_.text

    soup_category_ = BeautifulSoup(html_category_, "html.parser")
    all_products = []
    todays_data = []
    if soup_category_.find('h1') and 'We were not able to find a match. Try another search' in soup_category_.find(
            'h1').text:
        pass
    else:
        for product_ in soup_category_.findAll('div', {'class': "product-tile-set"}):
            try:
                rank_on_when_searched_brand = int(product_['item-index']) + 1
                url_this_ = product_.find('span', {'class': "description"}).find('a')['href']
                product_id = product_.find('input', {'name': "partNumb"})['value']
                title = product_.find('span', {'class': "description"}).text.strip()
                price = product_.find('div', {'class': "price"}).text.strip()

                this_product = {
                    'ProductId': product_id,
                    'Title': title,
                    'Price': price,
                    'Date': datetime.datetime.now().strftime("%m-%d-%Y"),
                    'url': url_this_,
                    'SearchTerm': search_term,
                }
                todays_data.append(this_product)
                this_product['PartitionKey'] = "Costco"

                hash_value = hashlib.md5(str(this_product['SearchTerm']).encode())

                this_product['RowKey'] = '{}-{}-{}'.format(hash_value.hexdigest(),
                                                           this_product['ProductId'],
                                                           str(datetime.datetime.now().strftime("%m-%d-%Y")))

                table_service.insert_or_replace_entity('CostcoTest', this_product)
            except Exception as e:
                this_exception = 'Error on line {} {} {}'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e)
                # logger.error(this_exception)
                print(this_exception)
                error_email += this_exception + '\n'

        yesterdaysdata = table_service.query_entities('CostcoTest',
                                                      filter="SearchTerm eq '{}' and Date eq '{}'".format(search_term, (
                                                              datetime.datetime.now() - datetime.timedelta(
                                                          1)).strftime("%m-%d-%Y")))

        for product_to in todays_data:
            found = False
            for prod_yest in yesterdaysdata:
                if product_to['ProductId'] == prod_yest['ProductId']:
                    found = True
                    if product_to['Price'] != prod_yest['Price']:
                        print('Price has Changed for this Product, Old: {}, New: {}'.format(prod_yest, product_to))
                        email_string + 'Price has Changed for this Product, Old: {}, New: {}\n'.format(prod_yest,
                                                                                                       product_to)
            if not found:
                print('New Product has been added: {}'.format(product_to))
                email_string += 'New Product has been added: {}\n'.format(product_to)

        for prod_yest in yesterdaysdata:
            found = False
            for product_to in todays_data:
                if product_to['ProductId'] == prod_yest['ProductId']:
                    found = True
            if not found:
                email_string += 'Product has been Removed: {}\n'.format(prod_yest)


def create_logger(blob):
    """Creates logger and handler, names log file, and sets formatting"""

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    logfile = now + "_" + blob + ".txt"

    logger = logging.getLogger('CostcoProductsScraper')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s:%(message)s')

    file_handler = logging.FileHandler('logs/' + logfile)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logfile, logger, file_handler


# Upload log file to blob storage
def upload_log(logfile, block_blob_service):
    """Upload log file to log blob

    Arguments:
        logfile: string, name of log file
        blob: string, name of folder in log blob to upload log into

    """
    log_path = "logs/" + logfile
    blob_path = "logs/CostcoProductsScraper"
    block_blob_service.create_blob_from_path(blob_path, logfile, log_path)


if __name__ == '__main__':
    try:
        block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

        # Check for logs folger
        if not (os.path.isdir("logs/")):
            os.mkdir("logs/")

        # Create log file
        logfile, logger, file_handler = create_logger('CostcoProductsScraper')

        start = datetime.datetime.now()
        logger.info("Starting Costco Products Scraper.")
        logger.info(start)
        weekly_category_scrap = False
        ca_scrap = False
        parser = argparse.ArgumentParser()
        parser.add_argument("-w", "--weekly", help="Use -w to run weekly category scrap.", action="store_true")
        parser.add_argument("-ca", "--canada", help="Use -c to run canada scrap.", action="store_true")
        args = parser.parse_args()
        if args.weekly:
            weekly_category_scrap = True

        if args.canada:
            ca_scrap = True

        # if True:  # not ca_scrap:
        #     login_costco()

        for partition_key, search_term in [
            ['Jump Starter', 'Jump Starter'],
            # ['Desk Lamp', 'Desk Lamp'],
            # ['Electric Bike', 'Electric Bike'],
            # ['Meat Thermometer', 'Meat Thermometer']
        ]:
            # if True:  # not ca_scrap:
            #     login_costco()
            try:
                main(logger, weekly_category_scrap, partition_key, search_term, ca_scrap)
            except Exception as e:
                this_exception = 'Error in Search Term `{}` on line {} {} {}'.format(search_term,
                                                                                     sys.exc_info()[-1].tb_lineno,
                                                                                     type(e).__name__, e)
                # logger.error(this_exception)
                print(this_exception)
                error_email += this_exception + '\n'

            # try:
            #     driver.close()
            #     driver.quit()
            #     is_popup_model_present = True
            #     path = 'C://chromedriver.exe'
            #     uc.install(executable_path=path)
            #     chrome_options = Options()
            #     chrome_options.add_argument("--log-level=3")
            #     chrome_options.add_argument("--start-maximized")
            #     chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', '--load-extension'])
            #     driver = webdriver.Chrome(options=chrome_options, executable_path=path)
            #     driver.implicitly_wait(2)
            # except:
            #     driver.close()
            #     driver.quit()

        # try:
        #     driver.close()
        #     driver.quit()
        # except:
        #     pass

        # Get end timestamp and log
        end = datetime.datetime.now()
        logger.info(end)
        print(end)

        # Log run time
        logger.info("Total Run time: " + str(end - start))
        print("Total Run time: " + str(end - start))

        # Upload log file to blob
        # upload_log(logfile, block_blob_service)

        # Delete log file
        try:
            file_handler.close()
            os.remove("logs/" + logfile)
        except Exception as ex:
            file_handler.open()
            logger.error(ex)
    except Exception as e:
        this_exception = 'Error on line {} {} {}'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e)
        # logger.error(this_exception)
        print(this_exception)
        error_email += this_exception + '\n'

    if error_email:
        email_subject = 'Costco_Products_scraper Error Alert - {}'.format(datetime.datetime.now().strftime('%m-%d-%Y'))

        username = 'datacollection@pjboren.com'
        password = 'ZipperBoots360'

        sendto = ['ajain@pjboren.com']
        cc = ['sdotloe@pjboren.com',
              'apawlak@pjboren.com',
              'pvijayvargiya@pjboren.com']

        # cc = [
        #     'pvijayvargiya@pjboren.com']

        # sendto = ['apawlak@pjboren.com']
        # cc = []

        sendto = ['ajain@pjboren.com']
        cc = []

        smtpsrv = "smtp.office365.com"
        smtpserver = smtplib.SMTP(smtpsrv, 587)

        smtpserver.starttls()
        smtpserver.login(username, password)

        msg = MIMEText(error_email)
        msg['Subject'] = email_subject
        msg['From'] = username
        msg['To'] = ', '.join(sendto)
        msg['CC'] = ', '.join(cc)

        # smtpserver.sendmail(msg=msg.as_string(), from_addr=username, to_addrs=(sendto + cc))
        smtpserver.close()

    if email_string:
        email_subject = 'Costco Comp Shop Product Change Alert - {}'.format(
            datetime.datetime.now().strftime('%m-%d-%Y'))

        username = 'datacollection@pjboren.com'
        password = 'ZipperBoots360'

        sendto = ['ajain@pjboren.com']
        cc = []

        smtpsrv = "smtp.office365.com"
        smtpserver = smtplib.SMTP(smtpsrv, 587)

        smtpserver.starttls()
        smtpserver.login(username, password)

        msg = MIMEText(email_string)
        msg['Subject'] = email_subject
        msg['From'] = username
        msg['To'] = ', '.join(sendto)
        msg['CC'] = ', '.join(cc)

        smtpserver.sendmail(msg=msg.as_string(), from_addr=username, to_addrs=(sendto + cc))
        smtpserver.close()

    sys.exit()
