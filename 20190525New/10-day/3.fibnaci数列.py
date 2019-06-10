# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 23:49
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.fibnaci数列.py

a = 1
b = 1
for i in range(5000):
    a,b = b,a+b
else:
    print(b)

def fbnc(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fbnc(num -1) + fbnc(num-2)


print(fbnc(5))