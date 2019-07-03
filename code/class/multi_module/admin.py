#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

from user import User

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
