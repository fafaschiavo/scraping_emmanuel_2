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
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

reload(sys)
sys.setdefaultencoding('utf-8')
print os.path.abspath(__file__)

lower_limit = int(sys.argv[1])
upper_limit = int(sys.argv[2])
csv_file_name = sys.argv[3]

print '_______________________________________________________________'
print 'Welcome to my scrapper - cdbaby time'
print '_______________________________________________________________'
total_band_array = []
total_name_appearances = []
repeated_counter = 0

#6868 - max pages
for page_number in xrange(int(lower_limit),int(upper_limit)):
	print 'Starting to scrape page ' + str(page_number)
	search_page = urllib2.urlopen('https://www.cdbaby.com/Top/p' + str(page_number))
	page_source = search_page.read()

	#detach first element - header
	raw_content = page_source.split('<div class="carousel-album">')[1:]

	bands_in_this_page = []
	for raw_element in raw_content:
		band_name = raw_element.split('class="carousel-album-artist-name clearfix">')[1].split('<!-- .carousel-album-container -->')[0].split('</span>')[0]
		band_name = band_name.lower()
		album_link = 'https://www.cdbaby.com' + raw_element.split('" href="')[1].split('"><img id="')[0]
		if band_name in total_name_appearances:
			repeated_counter = repeated_counter + 1
			print 'Repeate'
		else:
			total_name_appearances.append(band_name)
			bands_in_this_page.append([band_name, album_link])
	total_band_array.extend(bands_in_this_page)

	bands_data_frame = pd.DataFrame(total_band_array)
	bands_data_frame.columns = ['band_name', 'album_link']
	bands_data_frame.to_csv(csv_file_name, sep=';')
	print '----------'

print 'repetidas - ' + str(repeated_counter)
print 'total minerado - ' + str(len(total_band_array))
print '---------------- Finished! ----------------'

# python name_scrape_cdbaby.py 1 1500 band_name_1.csv
# python name_scrape_cdbaby.py 1500 3000 band_name_2.csv
# python name_scrape_cdbaby.py 3000 4500 band_name_3.csv
# python name_scrape_cdbaby.py 4500 6868 band_name_4.csv