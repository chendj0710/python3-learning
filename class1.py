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



class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


user1 = User('ergou', 'wang')
user2 = User('kangkang', 'li')

user1.descriper()
user1.greet_user()

admin1 = Admin('root', 'zhao', 'can add post')
admin1.show_privileges()
