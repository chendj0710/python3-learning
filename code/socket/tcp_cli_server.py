#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime
import os

'''对应的客户端是tcp_client.py'''
HOST = ''   #表示本机下所有地址，相当于c语言中的INADDR_ANY
PORT = 50001
BUFSIZE = 1024
MAX_LISTEN_NUM = 30
ADDR = (HOST, PORT)

server_fd = socket(AF_INET, SOCK_STREAM)
#设置端口可复用
server_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_fd.bind(ADDR)
server_fd.listen(MAX_LISTEN_NUM)
while True:
    print("Waiting for connection ...")
    client_fd, client_addr = server_fd.accept()
    print("...connected from :", client_addr)
    while True:
        #服务器端，deal cmd：data, os, ls <dir>
        rcv_buf = ''
        send_buf = ''
        data = client_fd.recv(BUFSIZE)
        if not data:  #client 断掉之后，则退出
            break;
        rcv_buf = data.decode('utf-8').strip()
        if rcv_buf == 'date':
            send_buf = ctime()
        elif rcv_buf == 'os':
            send_buf = os.name
        elif len(rcv_buf) >= 2 and rcv_buf[0:2] == 'ls':
            if len(rcv_buf) == 2:#cmd is ls
                file_dirs = os.listdir(os.curdir)
                for file_dir in file_dirs:
                    send_buf += file_dir
                    send_buf += '\r\n'
                #去除最后一个空行,rstrip并不修改自己，只是返将修改后的值返回
                send_buf = send_buf.rstrip()
                #print("%d %d" % (ord(send_buf[-2]),ord(send_buf[-1])))
            else:#ls <dir>
               dir = rcv_buf.split(' ', 1)[1]
               file_dirs = os.listdir(dir)
               for file_dir in file_dirs:
                   send_buf += file_dir
                   send_buf += '\r\n'
               send_buf = send_buf.rstrip()  #去除最后一个空行
        else:
            #print("Error cmd")
            send_buf = "Error cmd"
        #socket中的send需要传bytes流
        client_fd.send(send_buf.encode('utf-8'))
    client_fd.close()
server_fd.close()
