#!/usr/bin/env python
'UChatServer.py'

from socket import *
from time import strftime
import threading,sys

def server(sock, src, dst, size=1024):
    while True:
        try:
            #print('go go go!!!')
            #sock.sendto('server give A a message'.encode('ascii'),(src[0],12512))
            #sock.sendto('server give B a message'.encode('ascii'),(dst,12512))
            data, src= sock.recvfrom(BUFSIZ)
            if data.decode('ascii') == 'exit!':
                sock.close()
                print(repr(src),'socket close')
                return
            time = strftime('%H:%M:%S')
            data = repr(src[0]) + '  ' + time+'\n    '+data.decode('ascii')
            print(data)
            sock.sendto(data.encode('ascii'), (dst,12512))
        except timeout as e:
            pass
        except OSError as e:
            sock.close()
            return 	

#s = socket(AF_INET, SOCK_DGRAM)
#s.connect(('baidu.com', 0))
#HOST = s.getsockname()[0]
HOST = '192.127.0.1'
#HOST = '127.0.0.1'

PORT = 12512
BUFSIZ = 1024 
ADDR = (HOST, PORT)
usrs = [[1,'1','1',1,1]]

SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(ADDR)
SerSock.settimeout(1)
print('waiting connect...')
while True:
    try:
        dst, src = SerSock.recvfrom(BUFSIZ)
        print(repr(dst),repr(src))
        access = (dst.decode('ascii'),12512)
        print(("received from %s 's request") % repr(src))
        sock=socket(AF_INET, SOCK_DGRAM)
        sock.bind ((HOST,src[1]))
        print('bind address is ',HOST,src[1])	#look bind address
        sock.settimeout(1)
        print(('successfully bound with %s') % repr((HOST,src[1])))


        t=threading.Thread(target = server,args = (sock, src, dst))
        #usrs.append([sock, src, dst, t])
        t.start()
        print(repr(src) + 'have start server')	
    except timeout as e:
        pass
