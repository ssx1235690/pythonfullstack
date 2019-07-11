# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 23:38
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.partial.py


from functools import partial
import inspect

#### partial 函数对函数参数进行固定返回一个新函数

def add(x,y):
    return x+y

newadd = partial(add,x=50)
print(newadd(y=100,x=2222))
sig = inspect.signature(newadd)
params = sig.parameters.items()
print(params)