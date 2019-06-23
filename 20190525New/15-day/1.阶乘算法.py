# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 16:04
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.阶乘算法.py

import math
from functools import reduce
print(math.factorial(2))

print(reduce(lambda x,y:x*y,[1,2,3,4,5]))


# 杨辉三角的一个重要问题，求第n行第k个数的大小, 计算公式为 阶乘公式

list0 =  []

n = 5
k  =3
num = 1

for i in range(1,n+1):
    num = num * i
    if i== n or i == n - k or i == k:
        list0.append(num)
print(list0[2]//(list0[0]*list0[1]))

###  不考虑列表顺序， 应为结果为最大值 除于 两个小数的乘机




##### 矩阵转置


list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
for i in range(len(list1)):
    for j in range(i):
        list1[j][i],list1[i][j] = list1[i][j],list1[j][i]
print(list1)


