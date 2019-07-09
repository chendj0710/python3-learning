#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 50001
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    #socketservert默认是接收连接，处理请求，关闭连接的，所以，这边，我们需要每次都创建socket
    #类似于udp
    client_fd = socket(AF_INET, SOCK_STREAM)
    client_fd.connect(ADDR)
    tmp_str = input(">")
    if not tmp_str:
        continue;
    #因server端采用的是readline读信息，直到\r\n才返回，而input返回的字符串中不包含换行符，故此处手动加\r\n
    client_fd.send((tmp_str+"\r\n").encode('utf-8'))
    data = client_fd.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
    client_fd.close()
