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




# Here comes the main function
reset_ip()
print requests.get("http://icanhazip.com").text


# To get my IP address - https://icanhazip.com/
# 81.57.131.168 - meu IP
# 51.15.63.229
# 119.81.135.2
# 51.15.62.146