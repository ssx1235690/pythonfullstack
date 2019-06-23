# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 22:10
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.随机数判重.py

import random

enums = []
for i in range(2):

    enums.append(random.randrange(21))


print(enums)

sumlist = []
dfflist = []
state = [0] * len(enums)

for i in range(len(enums)):
    Flag = False
    if state[i]  == 1:
        continue
    for j in  range(i+1,len(enums)):
        if state[j] == 1:
            continue
        if enums[i] == enums[j]:
            state[i] = 1
            state[j] = 1
            Flag = True
    if Flag:
        sumlist.append(enums[i])
    else:
        dfflist.append(enums[i])
print(dfflist,sumlist)
