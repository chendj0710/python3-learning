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
