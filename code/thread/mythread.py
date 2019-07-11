#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
from  time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        #需要显示调用threading.Thread的__init__()函数
        #此处也可以使用显示调用父类函数，单此时必须传elf，threading.Thread.__init(self)
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        #获取函数func的返回值
        return self.res

    def run(self):
        #覆写Thread类的run函数
        print("Starting " + self.name + " at:" + ctime())
        self.res = self.func(*self.args)
        print(self.name + " finished at:" + ctime())
