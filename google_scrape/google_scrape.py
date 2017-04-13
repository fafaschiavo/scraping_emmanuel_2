from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import socks
import socket
import requests
import os
import time
import urllib2
import urllib
import subprocess
import pandas as pd
import csv
import xmllib
import cookielib
import sys
import json as m_json

def reset_ip():
	try:
		os.system("/etc/init.d/tor restart")
		time.sleep(1)
	except:
		pass

	socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
	socket.socket = socks.socksocket
	return None


print '_______________________________________________________________'
print 'Welcome to my scrapper - Google Version'
print '_______________________________________________________________'
total_band_array = []
total_link_array = []
csv_file_name = 'band_google_link_test_1000.csv'
lower_limit = 0
upper_limit = 1000

# Generate New IP from TOR
# reset_ip()
# print requests.get("http://icanhazip.com").text

succcess_counter = 0
total_band_array = pd.read_csv('band_name_1_backup.csv', error_bad_lines=False, delimiter=';')
total_band_array = total_band_array.drop('index', 1)

# tupelo blue

chromedriver = "/home/fabricio/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("https://www.google.com/")

for index, line in total_band_array.iterrows():
	if index > lower_limit and index < upper_limit:
		print '---------------'
		print 'Current mining - ' + str(index)
		print line['band_name']
		band_to_search = line['band_name'].decode('utf-8')
		search_term = band_to_search + ' band contact'
		search_field = browser.find_element_by_id("lst-ib")
		search_field.clear()
		search_field.send_keys(search_term)
		action = action_chains.ActionChains(browser)
		action.perform()
		action.send_keys(keys.Keys.ENTER)
		action.perform()
		time.sleep(2)
		page_source = browser.page_source

		total_result_array = []
		raw_elements = page_source.split('<div class="rc" data-hveid="')
		for raw_element in raw_elements[1:6]:
			try:
				new_link = raw_element.split('<cite class="_Rm">')[1].split('</cite>')[0]
				current_result = [band_to_search.encode('utf-8'), line['album_link'].encode('utf-8'), new_link.encode('utf-8')]
			except Exception as e:
				current_result = [band_to_search.encode('utf-8'), line['album_link'].encode('utf-8'), 'subindex_detected']
				print 'subindex_detected'

			total_link_array.append(current_result)
			bands_data_frame = pd.DataFrame(total_link_array)
			bands_data_frame.columns = ['band_name', 'album_link', 'google_link']
			bands_data_frame.to_csv(csv_file_name, sep=';')

print 'total minerado - ' + str(len(total_link_array))
print '---------------- Finished! ----------------'






# To get my IP address - https://icanhazip.com/
# 81.57.131.168 - meu IP Real