#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animals():
   def __init__(self, name):
       self.name = name

   def show(self):
       print("Animals print")

class Dog(Animals):
    #子类没有覆写__init__()，则会直接继承父类的
    def __init__(self, name):
       self.name = name

    def print_name(self):
        print(self.name)

    '''
    def show(self):
       print("Dog print")
    '''

    def my_default(self, *arg):
        #print("arg: " + str(arg[0]))
        print("default")

    '''
    #如果定义了__getattribute__, 则从父类继承的函数没有重写，则会报错
    def __getattribute__(self, name):
        print(name)
        #self.my_default(10)
    '''




dog = Dog('pen')
dog.print_name()
dog.show()

#显示调用父类中被覆写的函数
dog.__class__ = Animals
dog.show()
dog.__class__ = Dog
