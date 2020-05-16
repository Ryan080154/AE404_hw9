# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:38:07 2020

@author: Home
"""

import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://airtw,epa.gov.tw/")
time.sleep(1)
selectCountry = Select(chrome.find_element_by_id('ddl_county'))
selectCountry.select_by_index(1)
time.sleep(1)
selectSite = Select(chrome.find_element_by_id('ddl_site'))
selectSite.select_by_index(4)
time.sleep(1)


soup =BeautifulSoup(chrome.page_source,"html.parser")
air_info = soup.find_all('div',class_='info')[0]
state = air_info.find('h4').text[:6]
data = air_info.find('div',class_='date').text.strip()[:16]
PM25 = int(air_info.find('span',id = 'PM25').text)
air_quality = ''
if PM25<16:
    air_quality = "good"+' PM2.5 = '+str(PM25)
elif PM25<35:
    air_quality = "moderate"+' PM2.5 = '+str(PM25)
else:
    air_quality = "Unhealthy"+' PM2.5 = '+str(PM25)
webhook_key = "crMSGOLaQXRSNcKRYOXBQp"
trigger_name = "trigger1"
url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?valuel={}&value2={}&value3={}'.format(data,state,air_quality)
requests.get(url)
print(data,state,air_quality)