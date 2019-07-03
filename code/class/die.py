#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

from random import randint

class Die():
   def  __init__(self, sides=6):
       self.sides = sides

   def roll_die(self):
       print("\tThe random is " + str(randint(1, self.sides)))


die1 = Die()
print("The die' sides is：" + str(die1.sides))

num = 10
while num > 0 :
    die1.roll_die()
    num -= 1



die2 = Die(10)
print("The die' sides is：" + str(die2.sides))


num = 10
while num > 0 :
    die2.roll_die()
    num -= 1

die3 = Die(20)
print("The die' sides is：" + str(die3.sides))

num = 10
while num > 0 :
    die3.roll_die()
    num -= 1

die4 = Die(40)
print("The die' sides is：" + str(die4.sides))

for i in range(10):
    die4.roll_die()
