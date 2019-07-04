#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

filename = 'data/guest.txt'

file_object = open(filename, 'a')
while 1:
    user_name = input("please input guest name:")
    if user_name == 'q':
        break;
    file_object.write(user_name + '\n')
    print("Save OK.")

file_object.close()
