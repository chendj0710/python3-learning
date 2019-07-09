#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime
import sys


HOST = 'localhost'
PORT = 50001
#ADDR = (HOST, PORT)
BUFSIZE = 1024

#get server_ip & server_port
def get_ip_port():
    i = 1
    ip = HOST
    port = PORT
    while i < len(sys.argv):
        if(1 == i):
           ip = sys.argv[1]
        elif(2 == i):
           port = int(sys.argv[2])  #此处需要强转成int型
        else:#输入的参数超出两个
            print("usage:script <ip> <port>")
            sys.exit()
        i += 1
    return (ip, port)

#tcp client, get user's input and send to server, print msg recive from sever 
addr = get_ip_port()
client_fd = socket(AF_INET, SOCK_STREAM)
client_fd.connect(addr)
while True:
    tmp_str = input(">")
    if not tmp_str:
        continue;
    client_fd.send(tmp_str.encode('utf-8'))
    data = client_fd.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
client_fd.close()
