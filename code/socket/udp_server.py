#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 50002
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_ssock = socket(AF_INET, SOCK_DGRAM)
udp_ssock.bind(ADDR)
while True:
    data, addr = udp_ssock.recvfrom(BUFSIZE)
    if not data:
        continue;
    udp_ssock.sendto(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'), addr)
udp_ssock.close()
