# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:46:00 2021

@author: a
"""
import pywhatkit
#pywhatkit.sendwhatmsg("+917017524811", "Hi Nittu", 12, 58)
text="Awaaz kum kar"

pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
pywhatkit.sendwhatmsg("+919690675269", "text", 15, 3)


