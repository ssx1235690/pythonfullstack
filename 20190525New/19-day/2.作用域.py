# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 19:46
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.作用域.py


def outer():
    o = 65
    def inner():
        print('{}'.format(o))
        print(type(o))
    o += 1
    inner()
outer()

def outer():
    o = 65
    def inner():
        o = 97
        print('{}'.format(o))
        print(type(o))
    o += 1
    inner()
outer()


#### 全局变量和本地变量
x = 1
# def outer():
#     x += 1
#     print(x)
# UnboundLocalError: local variable 'x' referenced before assignmen
# outer()


### global 可以解决上述问题。但是不建议这么去用，很不好。

def outer():
    # x = 0
    global x
    x += 1
    print(x)
outer()


