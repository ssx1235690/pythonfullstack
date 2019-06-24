# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:14
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.选择排序和二元选择排序.py

# 选择排序和冒泡法的区别
# """
# （1）冒泡排序是比较相邻位置的两个数，而选择排序是按顺序比较，找最大值或者最小值；
#
# （2）冒泡排序每一轮比较后，位置不对都需要换位置，选择排序每一轮比较都只需要换一次位置；
#
# （3）冒泡排序是通过数去找位置，选择排序是给定位置去找数；
# """
import  random

list1 = [random.randint(1,155) for i in range(20)]
print(list1)

for i in range(len(list1)):
    min = i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[min]:
            min = j
    if min != i:
        tmp = list1[i]
        list1[i] = list1[min]
        list1[min] = tmp
print(list1)