#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from threading import Thread, Lock, BoundedSemaphore
from time import ctime, sleep
from atexit import register

'''范例：总共有5个槽用来放糖，然后一边生产一边卖'''
lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    '''生产者，增加计数'''
    lock.acquire()
    print("Refilling candy ...")
    try:
        candytray.release()
    except ValueError:          #BoundedSemaphore类型信号量， 当计数器超过初始值时，会抛出ValueError
        print("Full, skipping")
    else:
        print("OK")
    lock.release()

def buy():
    '''消费者, 减少计数'''
    lock.acquire()
    print("Buy candy...")
    if candytray.acquire(False):   #release(False), False表示，如果计数器为0，不阻塞，直接返回
         print("OK")
    else :
        print("Empty, skipping")
    lock.release()

def producer(nloops):
    for x in range(nloops):
        refill()
        sleep(randrange(3))   #随机延时3s以内

def consumer(nloops):
    for x in range(nloops):
        buy()
        sleep(randrange(3))

def main():
    '''创建生产者-消费者线程'''
    print("Starting at:" + ctime())
    print("The candy machine (full with %d bars)" % MAX)
    nloops = randrange(2,6)

    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2), )).start()  #buyer
    Thread(target=producer, args=(nloops, )).start()


@register
def _atexit():
    print("All done at:" + ctime())

if __name__ == '__main__':
    main()
