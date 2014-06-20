#!/usr/bin/env python
'UChatClient'
from socket import *
import threading
import time
import sys
from random import randint
import re

def isIP(ip=''):
	right ="^((\d|\d\d|[0-1]\d\d|2[0-4]\d|25[0-5])\.(\d|\d\d|[0-1]\d\d|2[0-4]\d|25[0-5])\.(\d|\d\d|[0-1]\d\d|2[0-4]\d|25[0-5])\.(\d|\d\d|[0-1]\d\d|2[0-4]\d|25[0-5]))$"
	#print(ip)
	#print(type(ip))
	if ip == '' :
		return False
	if re.match(right, ip) is not None:
		return True
	else:
		#print(m)
		return False
		
def recv(RevSock,BUFSIZ=1024):
	print('start recvive data')
	while True:
		try:
			data, aaa=RevSock.recvfrom(BUFSIZ)
			for count in range(len(data)):
				sys.stdout.write('\b \b')
				sys.stdout.flush()
			print(data.decode('ascii'))
		except timeout as e:
			#print('no receive data')
			pass
		except OSError:
			exit(0)
			pass

data = ''
def main():
	# get vistor ip and port
	visit = sys.argv.pop() if len(sys.argv) == 2 else '1.1.1.1' 
	i = isIP(visit)
	if i is False:
		print("your visit ip is wrong! you should check the ip")
		return
	
	# get my ip and port
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(('baidu.com', 0 ))
	Myip = s.getsockname()[0]
	s.close()
	MyPort = randint(20000, 60000)
	MyAddr = (Myip, MyPort)
	VisAddr = (visit, MyPort)
	print(MyAddr)

	Serip = '192.168.1.111'			#you should make sure the server ip is right
	SerPort = 12512
	SerAddr = (Serip, SerPort)
	Exit = False
			
	Sock = socket(AF_INET, SOCK_DGRAM)
	Sock.settimeout(1)
	Sock.bind(MyAddr)
	Sock.sendto(visit.encode('ascii'), SerAddr)

	RevSock = socket(AF_INET, SOCK_DGRAM)
	RevSock.settimeout(1)
	RevSock.bind((Myip, SerPort))

	print("programming have start.")
	print("if you want to exit the program,please input 'exit!' to leave the server\n")
	re = threading.Thread(target = recv, args=(RevSock,))
	re.start()

	while True:
		try:
			data = input()
		except (IOError,KeyboardInterrupt):
			print('input error!!')
		if data == 'exit!':
			print()
			Sock.sendto('exit'.encode('ascii'),SerAddr)
			Sock.close()
			print('send socket have closed')
			RevSock.close()
			print('receive socket have closed')
			#print('now you can close the window')
			exit(0)
		if not len(data) == 0:
			Sock.sendto(data.encode('ascii'),(Serip,MyPort))
			#print('data have sended')

if __name__ == '__main__':
	main()
	
