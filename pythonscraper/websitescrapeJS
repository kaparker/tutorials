#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:43:54 2018

@author: kerry
"""
# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt' 
print(urlpage)

# scrape the webpage using beautifulsoup
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find product items
results = soup.find_all('div', attrs={'class': 'listing category_templates clearfix productListing'})
print('BeautifulSoup - Number of results', len(results))
# since the page uses javascript returns 0 results


# scraoe the webpage using firefox webdriver
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox(executable_path = '/Users/kerry/Downloads/geckodriver')
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('Firefox Webdriver - Number of results', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})
# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('asdaYogurtLink.csv')


# scraoe the webpage using phantomJS webdriver
# use phantomJS webdriver
driver = webdriver.PhantomJS(executable_path = '/Users/kerry/Downloads/phantomjs')
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('PhantomJS Webdriver - Number of results', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})
# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('asdaYogurtLinkPJS.csv')

# scraoe the webpage using headless webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

# use firefox as a headless browser
driver = webdriver.Firefox(executable_path = '/Users/kerry/Downloads/geckodriver', firefox_options=options)
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('PhantomJS Webdriver - Number of results', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})
# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('asdaYogurtLinkHeadless.csv')


# get data making request to API
# import extra libraries
import json

# request url
urlreq = 'https://groceries.asda.com/api/items/search?keyword=yogurt'
# get response
response = urllib.request.urlopen(urlreq)
# load as json
jresponse = json.load(response)
# write to file as pretty print
with open('asdaresp.json', 'w') as outfile:
    json.dump(jresponse, outfile, sort_keys=True, indent=4)