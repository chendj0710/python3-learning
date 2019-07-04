#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = 'data/pi_digits.txt'
filename2 = 'data/learning_python.txt'

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


#readlines, 并将内容合并
print("read file by lines:")
with open(filename) as file_object:   #file_object只在with这个块内有效
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print("pi_string:" + pi_string + ", len(pi_string):" + str(len(pi_string)))

#print("Enter your birth, in the form yymmdd:")
birth_day = input("Enter your birth, in the form yymmdd:")
if birth_day in pi_string:
    print("Your birthday appears in the digits pi")
else:
    print("Your birthday doesn't appears in the digits pi")

print("\nopen learning_python.txt, and replace Python by C:")
with open(filename2) as file_object:
    #此处的in相当于strncmp，区分大小写
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())
