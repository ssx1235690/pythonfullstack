# -*- coding: utf-8 -*-
# @Time    :  2019/5/25 16:59
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.杨辉三角.py

import math


# 判断素数
num = int(input('give me your num:  '))
list = []
for i in range(2,math.ceil(num*0.5)):
    if num % i == 0:
        break
else:
    print(num)

# 求100以内素数的和
sum = 0
for i in range (1,100):
    for j in range(2,math.ceil(i * 0.5)):
        if i% j == 0:
            break
    else:
        sum += i
else:
    print(sum)


############## 元组 tuple

# t1 = ([1,2],23,342)
# t1[0][1] = 0

# l1 = [(2,3),89234,234]
# l1[0][1] = 5


########## name tuple
import collections

t2  = collections.namedtuple('t2',['x','y'])
zz = t2(1,2)
print(zz.x)