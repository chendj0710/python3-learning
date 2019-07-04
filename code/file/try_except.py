#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_words(filename):
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


files = ['data/learning_python.txt', 'data/learning_c.txt']
for file in files:
    count_words(file)
