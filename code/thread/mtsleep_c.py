#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
from time  import sleep, ctime

loops = [4,2]

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
        threads[i].join()   #执行到此处后，则主线程会一直阻塞，直到threads[i]线程结束
        #print("i = "+str(i) + ", at:" + ctime())

    print("All done at:" + ctime())

'''********************方法2：创建一个实例，并传给它一个可调用实例*****************************'''
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):   #覆写__call__函数，则表示其实例可调用
        #因args是一个元组，如上面的(i, loops[i])，而我们定义的loop是一个固定参数的
        #此处将其解包，拆分成nloop和nsec两个参数，故使用*self.args
        self.func(*self.args)

def main2():
    print("Starting at: " + ctime())
    threads = []
    nloops = range(len(loops)) #获取一个0-2的序列
    for i in nloops:
        #创建一个线程，并传递一个可调用的类，在内部会调用类的__call__()函数
        #loop.__name__ 函数名
        #print("loop.__name__:" + loop.__name__)
        tid = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(tid) #存储线程号

    for i in nloops:
        threads[i].start()  #start 线程

    for i in nloops:
        threads[i].join()   #执行到此处后，则主线程会一直阻塞，直到threads[i]线程结束
        #print("i = "+str(i) + ", at:" + ctime())

    print("All done at:" + ctime())

'''********************方法3：派生Thread子类，并创建子类的实例*****************************'''
'''
派生Thread子类和给Thread传类的区别
1.派生子类需要在__init__调用Thread的__init__()
2.派生子累重写Thread的run函数，再次调用传入的线程函数
'''
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        #需要显示调用threading.Thread的__init__()函数
        #此处也可以使用显示调用父类函数，单此时必须传elf，threading.Thread.__init(self)
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        #覆写Thread类的run函数
        self.func(*self.args)

def main3():
    print("Starting at: " + ctime())
    threads = []
    nloops = range(len(loops)) #获取一个0-2的序列
    for i in nloops:
        #创建一个线程，并传递一个可调用的类，在内部会调用类的__call__()函数
        #loop.__name__ 函数名
        tid = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(tid) #存储线程号

    for i in nloops:
        threads[i].start()  #start 线程

    for i in nloops:
        threads[i].join()   #执行到此处后，则主线程会一直阻塞，直到threads[i]线程结束
        #print("i = "+str(i) + ", at:" + ctime())

    print("All done at:" + ctime())

if __name__ == '__main__':
    #main1()
    main2()
