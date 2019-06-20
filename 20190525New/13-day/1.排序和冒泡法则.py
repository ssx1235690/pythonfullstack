# -*- coding: utf-8 -*-
# @Time    :  2019/6/20 9:49
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.排序和冒泡法则.py

import  random
# nums = input('give me  three nums: ')

list_nums = []
for i in range(100):
        list_nums.append(random.randrange(1,90))

# list_nums = nums.split()


# list_nums.sort(key=int)
# print(list_nums)
# print(list_nums.reverse())


# print(sorted(list_nums))
print(list_nums)
print(max(list_nums))
count_swap = 0
count  = 0
for i in range(list_nums.__len__()):
    flag = False   # 本来已经符合的序列不会进行重复比较计算
    for j in range(list_nums.__len__() - i - 1):
        if list_nums[j] < list_nums[j+1]:
            count += 1
            tmp = list_nums[j+1]
            list_nums[j+1] = list_nums[j]
            list_nums[j] = tmp
            count_swap += 1
            flag = True
    if not flag:
        break
print(list_nums,count_swap,count,sep='\n')