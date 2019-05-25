# -*- coding: utf-8 -*-
# @Time    :  2019/5/25 16:59
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.杨辉三角.py

import math

num = int(input('give me your num:  '))
list = []
for i in range(math.ceil(num*0.5),num):
    if num % i == 0:
        break
    else:
        print(num)
        break