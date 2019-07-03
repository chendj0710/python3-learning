#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

from user import User
from admin import Admin


user1 = User('ergou', 'wang')
user2 = User('kangkang', 'li')

user1.descriper()
user1.greet_user()

admin1 = Admin('root', 'zhao', 'can add post')
admin1.privileges.show_privileges()
