#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
from time  import sleep, ctime

loops = [2,4]

def loop(nloop, nsec):
    #延时函数，延时nsec秒
    print("Start loop " + str(nloop) + " at:" + ctime())
    sleep(nsec)
    print("loop " + str(nloop) + " done at:" + ctime())

'''********************方法1：创建一个实例，并传给它一个函数*****************************'''
def main1():
    print("Starting at: " + ctime())
    threads = []
    nloops = range(len(loops)) #获取一个0-2的序列
    for i in nloops:
        #创建一个线程，并注册执行函数和参数
        tid = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(tid) #存储线程号

    for i in nloops:
        threads[i].start()  #start 线程

    for i in nloops:
        threads[i].join()   #执行到此处后，则主线程会一直阻塞，知道threads[i]线程结束
        #print("i = "+str(i) + ", at:" + ctime())

    print("All done at:" + ctime())

'''********************方法2：创建一个实例，并传给它一个可调用的类*****************************'''

if __name__ == '__main__':
    #main1()
