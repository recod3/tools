#!/usr/bin/env python
#################################
#### SCAN SSHtool  #######
## By @zon3r/recod3 #######
#-------------####

import socket

###----------- Banner in request HTTP --------------###
def retBanner(ip, port):

  try:
            socket.setdefaulttimeout(1)
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024)
            return banner
	except:
	    return

###------------------Scan Service ------------------###
# Range default: 192.168.1.0/255 | ip ="xxx.xxx.xxx."
# Port range: portList[port1,port2,port3,..portX]

def main():
	portList = [22]
	for x in range(0, 255):
		ip = '192.168.1.' + str(x)
		for port in portList:
			banner = retBanner(ip, port)
			if banner:
				print '[+]  ' + ip + ': ' + str(banner)

###-----------------------MAIN----------------------###
if __name__ == '__main__':
	print "[+]Search  service SSH in LAN ..."
	main()
	print "[+]Search  terminate ......[OK]"
