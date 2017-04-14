import socks
import socket
import requests
import os
import time

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

# Generate New IP from TOR
reset_ip()
print 'Hello'
print requests.get("http://icanhazip.com").text

succcess_counter = 0
total_band_array = pd.read_csv('band_name_1 backup.csv', error_bad_lines=False, delimiter=';')
total_band_array = total_band_array.drop('index', 1)

for index, line in total_band_array.iterrows():
	print index
	print line






# To get my IP address - https://icanhazip.com/
# 81.57.131.168 - meu IP Real