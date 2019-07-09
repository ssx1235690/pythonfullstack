# -*- coding: utf-8 -*-
# @Time    :  2019/7/3 15:44
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.类型注解.py


def add(x:int,y:int):
    """
    :param x:
    :param y:
    :return:
    """
    return x + y

print(help(add))
print(add(1,2))
print(add.__annotations__)
print(add.__annotations__['x'])
print(type(add.__annotations__['x']))

#### 为了不改变python 动态语言的性质，没有对参数的类型作强制判断

from inspect import  signature


def foo(a, *, b:int, **kwargs):
    pass+
sig = signature(foo)
print(str(sig))


print(str(sig.parameters['b']))