#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''   #表示本机下所有地址，相当于c语言中的INADDR_ANY
PORT = 50001
ADDR = (HOST, PORT)


class MyRequstHandler(SRH):
    #覆写StreamRequestHandler中的handle,缺省是空函数
    def handle(self):
        print("...connected from :", self.client_address)
        self.wfile.write((("[%s] %s") %
            (ctime(), self.rfile.readline().strip().decode('utf-8'))).encode('utf-8'))

tcp_serv = TCP(ADDR, MyRequstHandler)
print("Waiting for connection ...")
tcp_serv.serve_forever()
