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
