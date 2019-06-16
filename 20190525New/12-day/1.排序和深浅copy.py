# -*- coding: utf-8 -*-
# @Time    :  2019/5/25 19:10
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.排序和深浅copy.py


## 内容相同  ， 地址相同

list0 = list(range(5))
list1 = list(range(5))
list2 = list0

print(list1 == list2)

list2[2] = 'adf'
print(list0,list1,list2,sep='\n')


import  copy

list0 = list(range(5))
list1 = list(range(5))
list2 = copy.deepcopy(list0)

print(list1 == list2)

list2[2] = 'adf'
print(list0,list1,list2,sep='\n')
