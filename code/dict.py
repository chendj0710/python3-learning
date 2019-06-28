#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

#create dict
#alien_0 = {'color':'green', 'points':5}
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#add key:value
alien_0['x-postion'] = 0
alien_0['y-postion'] = 5
print(alien_0)

#multi lines for dict
favorite_languages = {
    'jen':'c',
    'sarah':'python',
    'edward':'ruby',
    'phil':'python',
}

print(favorite_languages)

print("sarah's favorite language is " +
    favorite_languages['sarah'] +
    ".")

#exercise
#1.person info
my_wife = {
    'name':'wangergou',
    'age':'18',
    'city':'nanjing',
    'interst':'drink Milk tea',
}
print(my_wife)

del my_wife['age']
print(my_wife)

#add item
my_wife['age'] = 18
print(my_wife)

#reverse
for key in my_wife.keys():
    print(key)

#sorted
for key in sorted(my_wife.keys()):
    print(key)


#字典和列表的嵌套
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese'],
}

print("you order a " + pizza['crust'] + "-crust pizza " +
        "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#访问字典中的某列表的指定下标元素
print(pizza['toppings'][1])
