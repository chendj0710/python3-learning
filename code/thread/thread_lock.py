#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from threading import Thread, currentThread, Lock
from time import ctime, sleep
from atexit import register

class CleanOutputSet(set):
    def __str__(self):
        #str.join(sequence)  str中是间隔符，jion用于将序列中的元素以指定的字符连接生成一个新的字符串
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3, 7)))  #随机生成3~6个数，添加到loops中，每个值的范围时2~4
remaining = CleanOutputSet()

def loop(nsec):
    my_name = currentThread().name

    #获取锁，修改全部变量，并输出
    lock.acquire()
    remaining.add(my_name)
    print("%s Stared %s" % (ctime(), my_name))
    lock.release()

    sleep(nsec)
    lock.acquire()
    remaining.remove(my_name)
    print("%s finished %s (%d sec)" % (ctime(), my_name, nsec))
    print("(remaining:%s)" % (remaining or 'NONE'))  #remaining为空，则为False
    lock.release()

def main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

#使用register，注册一个退出函数，当脚本退出时调用
@register
def _atexit():
    print("All done at:" + ctime())

if __name__ == '__main__':
    main()
