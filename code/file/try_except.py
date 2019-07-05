#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_words(filename):
    """统计文件中的单词数"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        #print("Sorry, The file " + filename + "doesn't exist.")
        pass  #站位符，do nothing
    else:
        words = content.split()    #split 按空格拆分，返回字符串列表
        num_words =  len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")
        return num_words


'''
块注释， 三个单引号
此处是count_words函数的测试
files = ['data/learning_python.txt', 'data/learning_c.txt']
for file in files:
    count_words(file)
'''

#循环读取用户输入的数，并对两数求和
print("please input two nums, and input q for quit")
while True:
    try:
        input_str = input("first num:")
        num1 = int(input_str)
    except ValueError:
        print("Type error, please input digits.")
        continue
    try:
        input_str = input("second num:")
        num2 = int(input_str)
    except ValueError:
        print("Type error, please input digits.")
        continue
    #print("sum is:" + str(sum_nums(num1, num2)))
    print("sum is:" + str(num1+num2))
