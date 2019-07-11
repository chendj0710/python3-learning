#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange, randint
from time import ctime, sleep
from queue import Queue
from atexit import register
from mythread import MyThread

def readQ(queue):
    val = queue.get(True)
    print("Read queue, get val:%s, queue size now %d"
            % (str(val), queue.qsize()))
    return val

def writeQ(queue, val):
    queue.put(val)
    print("Write queue, write val:%s, queue size now %d"
          % (str(val), queue.qsize()))

def reader(queue, nloops):
    for x in range(nloops):
        readQ(queue)
        sleep(randint(2, 5))   #randint 在[a,b]之间产生随机数，两边都是闭


def writer(queue, nloops):
    for x in range(nloops):
        writeQ(queue, randrange(10))
        sleep(randint(1,3))

funcs = [reader, writer]
nfuncs = range(len(funcs))     #产生函数列表对应的下标序列， 0,1

def _main():
    nloops = randint(2, 5)
    q = Queue(100)

    threads = []
    for i in nfuncs:
        tid = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(tid)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print("All done")

if __name__ == '__main__':
    _main()
