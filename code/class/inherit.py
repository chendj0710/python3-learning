#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animals():
   def __init__(self, name):
       self.name = name

class Dog(Animals):
    #子类没有覆写__init__()，则会直接继承父类的
    def print_name(self):
        print(self.name)


dog = Dog('pen')
dog.print_name()
