#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#create names list
names = ['zhangsan', 'wagner', 'mazi', 'lisi']


#treavesing list
for name in names:
    print(name + ', that was a great man')

print('Thank you, everybody')


#数字列表
squares = [value**2 for value in range(1, 6) ]
print(squares)

#print 1-1000000
nums = list(range(1, 1000001))
print(nums)

print('nums min:' + str(min(nums)) + ', max:' + str(max(nums)))
print('sum(nums):' + str(sum(nums)))

#print 1-20间的基数
for num in range(1, 20, 2):
    print(num)

#create list 1-10 的立方
nums = [value**3 for value in range(1, 11)]
print(nums)

#treavesing 切片list
for num in nums[:3]:
    print(num)

#降序输出nums前三
for num in sorted(nums, reverse=True)[:3]:
    print(num)


#将列表1中所有元素追加到列表2中
#定义一个待验证用户表和已验证用户列表
unconfirmed_users = ['zhangsan', 'lisi', 'wanger', 'mazi']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print("Verifying user: " + user.title())
    confirmed_users.append(user)

#print all confirmed user
for user in confirmed_users:
    print(user.title())


#删除某个值， 从列表中
animals = ['dog', 'cat', 'monkey', 'cat', 'pig', 'cat']
tmpAnimal = 'cat'

while tmpAnimal in animals:
    animals.remove(tmpAnimal)

print(animals)


#法二
i = 0
while i < len(animals):
    if(animals[i] == tmpAnimal):
        animals.remove(tmpAnimal)
    i += 1


print(animals)
