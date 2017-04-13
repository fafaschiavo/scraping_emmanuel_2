# -*- coding: latin-1 -*-
import os
import urllib2
import urllib
import subprocess
import pandas as pd
import requests
import csv
import xmllib
import cookielib
import re

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


print '_______________________________________________________________'
print 'Welcome to my scrapper - Individual Version'
print '_______________________________________________________________'
succcess_counter = 0
total_band_array = pd.read_csv('band_google_link_test_1000.csv', error_bad_lines=False, delimiter=';')
total_band_array = total_band_array.drop('index', 1)

page_url = 'http://www.venicetheband.com/?Contact'
print 'Starting to scrape page ' + str(page_url)
search_page = urllib2.urlopen(page_url)
page_source = search_page.read()

matches = re.findall(r'[\w\.-]+@[\w\.-]+', page_source);

if len(matches) == 0: 
   print 'I did not find anything'
else:
   print 'My string is in the html'
   print matches


# for index, line in total_band_array.iterrows():
# 		print line['google_link']