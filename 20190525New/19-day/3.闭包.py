# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 20:28
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.闭包.py

# 闭包的概念就是内嵌函数使用了 外部函数的变量就叫闭包


def outer():
    x = 100
    def inner():
        print(x)
    return  inner
outer()()

### 全局变量并不影响我们的闭包
x = 1000
outer()()


#### python3提供了nonlocal 方式对 外部变量进行修改

def outer():
    x = 100
    def inner():
        nonlocal  x
        x += 1
        print(x)
    return  inner
outer()()


