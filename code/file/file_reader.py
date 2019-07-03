#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

filename = 'data/pi_digits.txt'

#read all to mem
print("read file all:")
#with可以在程序不再使用文件时，自动调用close，关闭文件，即使是程序抛异常的情况下
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


#read by line
print("read file by line:")
with open(filename) as file_object:
    for line in file_object:
        print(line)

#read by line  remove the space
print("read file by line and strip space:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
