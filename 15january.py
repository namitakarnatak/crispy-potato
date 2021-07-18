# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 06:29:13 2021

@author: a
"""

import requests

URL = 'https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen'
page = requests.get(URL)
