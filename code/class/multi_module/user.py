#!/usr/bin/env python3
# -*- coding: utf-8 -*-\


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def descriper(self):
        print("first name: " + self.first_name)
        print("last name: " + self.last_name)
        print("")

    def greet_user(self):
        print("Hi, " + self.first_name + " " + self.last_name)
        print("")
