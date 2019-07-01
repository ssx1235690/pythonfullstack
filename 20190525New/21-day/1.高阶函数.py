# -*- coding: utf-8 -*-
# @Time    :  2019/6/30 14:29
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.高阶函数.py

# 高阶函数的概念: 1 接受一个或3多个函数输入  2输出一个函数  满足下列两条之一


def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


f1 = counter(10)
f2 = counter(10)

print(f1==f2)
print(f1 is f2)
print(f1() is f2())

print(f1())
print(f1())
print(f1())
print(f1())
print(f2())
