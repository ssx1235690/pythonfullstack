# -*- coding: utf-8 -*-
# @Time    :  2019/5/25 16:59
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.杨辉三角.py

import math


# # 判断素数
# num = int(input('give me your num:  '))
# list = []
# for i in range(2,math.ceil(num*0.5)):
#     if num % i == 0:
#         break
# else:
#     print(num)
#
# # 求100以内素数的和
# sum = 0
# for i in range (1,100):
#     for j in range(2,math.ceil(i * 0.5)):
#         if i% j == 0:
#             break
#     else:
#         sum += i
# else:
#     print(sum)
#
#
# #  三角打印
#


import sys
import time
times1= time.time()
sys.setrecursionlimit(100000)
def genlist(listx):
    listsum = [1,1]
    for i in range(0,len(listx)-1):
        listsum.insert(-1,listx[i]+listx[i+1])
    return listsum

def sanjiao(x):
    if x == 1 :
        return  [1]
    elif x == 2 :
        return [1,1]
    else:
        return  genlist(sanjiao(x-1))


num = input('需要打印几行杨辉： ')
num = int(num)
for i in range(1,num+1):
    print('  '*(num - i),end='')
    for j in sanjiao(i):
        print(j,end='   ')
    print()


##### 迭代法

print([1])
print([1,1])

pre = [1,1]

num = int(input('需要打印几行杨辉： '))

for i in range(num-2):
    new = [1]
    for i in range(len(pre)-1):
        new.append(pre[i]+pre[i+1])
    else:
        new.append(1)
    print(new)
    pre = new
