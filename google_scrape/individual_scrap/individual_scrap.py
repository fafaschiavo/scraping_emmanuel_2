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
from validate_email import validate_email
import time

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
csv_file_name = 'email_address_raw.csv'
start_time = time.time()
succcess_counter = 0
total_band_array = pd.read_csv('band_google_link_test_1000.csv', error_bad_lines=False, delimiter=';')
total_band_array = total_band_array.drop('index', 1)
total_link_array = []

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

for index, line in total_band_array.iterrows():
	page_url = line['google_link']

	if page_url != 'subindex_detected':
		print '---------------------'
		print 'Analyzing page - ' + str(index) + '\n'
		print 'Total found so far - ' + str(succcess_counter)
		print("--- %s seconds ---" % (time.time() - start_time))
		if'http' in page_url:
			pass
		else:
			page_url = 'http://' + page_url

		print 'Scraping this link - ' + str(page_url)

		try:
			search_page = urllib2.Request(page_url, headers=hdr)
			page_source = urllib2.urlopen(search_page).read()

			matches = re.findall(r'[\w\.-]+@[\w\.-]+', page_source);

			if len(matches) == 0: 
				print 'Nothing found...'
			else:
				flag = False
				for email_address in matches:
					if validate_email(email_address, check_mx=True) != False:
						print email_address
						flag = True
						current_result = [line['band_name'].encode('utf-8'), line['album_link'].encode('utf-8'), line['google_link'].encode('utf-8'), email_address]
						total_link_array.append(current_result)
						bands_data_frame = pd.DataFrame(total_link_array)
						bands_data_frame.columns = ['band_name', 'album_link', 'google_link', 'email_address']
						bands_data_frame.to_csv(csv_file_name, sep=';')
					if flag:
						succcess_counter = succcess_counter + 1
		except:
			pass
		




# page_url = 'http://www.venicetheband.com/?Contact'