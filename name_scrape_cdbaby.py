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

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


print '_______________________________________________________________'
print 'Welcome to my scrapper - cdbaby time'
print '_______________________________________________________________'
total_band_array = []
total_name_appearances = []
repeated_counter = 0

for page_number in xrange(1,6868):
	print 'Starting to scrape page ' + str(page_number)
	search_page = urllib2.urlopen('https://www.cdbaby.com/Top/p' + str(page_number))
	page_source = search_page.read()

	#detach first element - header
	raw_content = page_source.split('<div class="carousel-album">')[1:]

	bands_in_this_page = []
	for raw_element in raw_content[:-2]:
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
	bands_data_frame.to_csv('band_name.csv', sep=';')
	print '----------'

print 'repetidas - ' + str(repeated_counter)
print 'total minerado - ' + str(len(total_band_array))
print '---------------- Finished! ----------------'