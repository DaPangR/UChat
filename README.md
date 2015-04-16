
This is UDP chat program. It only can work in LAN.

使用说明：
1.先运行UChatSer.py，即python UChatSer.py
2.然后修改UChatCli.py的第57行，将Serip改成，UChatSer.py运行机器所在的ip.
3.运行UChatCli.py,后面加上欲访问电脑的IP，即python UChatCli.py <目标机器的IP>
4.如果想要结束客户端，需要输入 "exit!",否则套接字不能关闭，下次运行客户端也许会出现问题。

注意：此程序的客户端和服务端不能运行在同一台电脑上，即不能用电脑的环路IP进行测试。

注意：如果只运行一个客户端，并不能实现通话。必须要两个客户端同时运行才能完成会话。如果只运行一个客户端，服务端会告诉你你欲访问的电脑没有上线。
