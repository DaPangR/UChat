#!/usr/bin/env python
'UChatServer.py'

from socket import *
from time import strftime
import threading,sys

def server(sock, access, addr, size=1024):
    while True:
        try:
            #print('go go go!!!')
            #sock.sendto('server give A a message'.encode('ascii'),addr)
            #sock.sendto('server give B a message'.encode('ascii'),access)
            data, addr = sock.recvfrom(BUFSIZ)
            time = strftime('%H:%M:%S')
            data = repr(addr[0]) + '  ' + time+'\n    '+data.decode('ascii')
            print(data)
            sock.sendto(data.encode('ascii'), access)
        except timeout as e:
            pass
        except OSError as e:
            return 	

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('baidu.com', 0))
HOST = s.getsockname()[0]
#HOST = '192.127.0.1'
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
        access, addr = SerSock.recvfrom(BUFSIZ)
        for i in range( len(usrs) ):
            if addr[0] in usrs[i][1]:
                usrs[i][0].close()
                usrs.remove(usrs[i])
                for j in range( len(usrs) ):
                    if addr[0] in usrs[j][2]:
                        SerSock.sendto('\n->your vistor have log out,now he will not receive your message'.encode('ascii'),usrs[j][1])
                print(repr(addr),'hava remove from server')
                break
            else:
                access = (access.decode('ascii'),12512)
                print(("received from %s 's request") % repr(addr))
                sock=socket(AF_INET, SOCK_DGRAM)
                sock.bind ((HOST,addr[1]))
                print('bind address is ',HOST,addr[1])	#look bind address
                sock.settimeout(1)
                cli_addr = (addr[0], 12512)				#client recevie address
                print(('successfully bound with %s') % repr(cli_addr))

                for i in range( len(usrs) ):
                    if access[0] in usrs[i][1]:
                        SerSock.sendto("\nyour vistor have connect with server,so your message him can recevie".encode('ascii'),cli_addr)		
                        isonline = True
                        break
                else:
                    SerSock.sendto("\nyour vistor don't connect with server,so your message him can't recevie".encode('ascii'),cli_addr)		
                    isonline = False

                for i in range( len(usrs) ):	#check this client's IP is or not in other's access
                    if addr[0] in usrs[i][2] and usrs[i][4] == False:
                        SerSock.sendto('\n->your vistor has log on,now he can recevie your message\n'.encode('ascii'),usrs[i][1])
                        usrs[i][4] = True

                t=threading.Thread(target = server,args = (sock, access, cli_addr))
                usrs.append([sock, cli_addr, access, t, isonline])
                t.start()
                print(repr(addr) + 'have start server')	
    except timeout as e:
        pass
