# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 21:30
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 5.函数销毁.py


def outer():
    x = 100
    def inner():
        nonlocal  x
        x += 1
        print(x)
    return  inner
lele = outer()

del lele

print(outer())