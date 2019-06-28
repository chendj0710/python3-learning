#!/usr/bin/env python3
# -*- coding: utf-8 -*-\


#def a add fun
def my_increase(num):
    num += 1

num = 10
my_increase(num)
print(num)   #输出10，说明python是采用传值的


#任意数量的关键字实参
def print_table(**tableInfo):
    for key, value in tableInfo.items():
        print(key.title() + ":" + str(value))  #str如果检测到时串，则直接返回


print_table(groupno='1', groupName='link1')
print_table(groupno=1, groupName='link1')
