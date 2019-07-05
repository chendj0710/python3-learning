#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 50001
BUFSIZE = 1024
MAX_LISTEN_NUM = 30
ADDR = (HOST, PORT)

client_fd = socket(AF_INET, SOCK_STREAM)

client_fd.connect(ADDR)
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
