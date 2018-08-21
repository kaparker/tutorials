#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:44:37 2018

@author: kerry
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv

# specify the url
urlpage = 'https://www.lseg.com/resources/1000-companies-inspire/2018-report-1000-companies-uk/search-1000-companies-uk-2018?results_per_page=1000'

print(urlpage)
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
results = soup.find_all('div', attrs={'class': 'tabular-data-panel'})
#print('Number of results', len(results))


rows = []
rows.append(['Company Name', 'Website', 'Sector', 'Region', 'Revenue Band'])

for result in results:
    data = result.find_all('span', attrs={'class': 'panel-row-text'})
    companyName = data[0].getText()
    website = data[1].getText()
    sector = data[2].getText()
    region = data[3].getText()
    revenueBand = data[4].getText()
    
    rows.append([companyName, website, sector, region, revenueBand])

# Create csv and write rows to output file
with open('lseg.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
   