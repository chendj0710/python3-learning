#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''   #表示本机下所有地址，相当于c语言中的INADDR_ANY
PORT = 50001
BUFSIZE = 1024
MAX_LISTEN_NUM = 30
ADDR = (HOST, PORT)

server_fd = socket(AF_INET, SOCK_STREAM)
server_fd.bind(ADDR)
server_fd.listen(MAX_LISTEN_NUM)
while True:
    print("Waiting for connection ...")
    client_fd, client_addr = server_fd.accept()
    print("...connected from :", client_addr)
    while True:
        data = client_fd.recv(BUFSIZE)
        if not data:  #client 断掉之后，则退出
            break;
        #socket中的send需要传bytes流
        client_fd.send(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'))
    client_fd.close()
server_fd.close()
