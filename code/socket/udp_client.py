#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 50002
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_csock = socket(AF_INET, SOCK_DGRAM)
#test socket.getservbyname(), socket包中的公共函数，非类中函数
daytime_port = getservbyname('daytime', 'udp')
print("daytime_port:" + str(daytime_port))
while True:
    buf = input(">")
    #udp是无连接的，一个UDP客户端，可以创建一个套接口并发送数据包给一个服务器
    #然后用同一个套接口发送另一个数据给另一个服务器，即套接口和服务器无绑定
    #当时tcp是有连接的，一个套接口对应一个服务器。
    udp_csock.sendto(buf.encode('utf-8'), ADDR)
    data,addr = udp_csock.recvfrom(BUFSIZE)
    if not data:
        break;
    print(data.decode('utf-8'))
udp_csock.close()
