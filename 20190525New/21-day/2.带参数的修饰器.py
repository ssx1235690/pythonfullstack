# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 23:19
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.带参数的修饰器.py


### 柯里化  f(x+y) = f(x)(y)

import datetime

def add(x):
    def xxx(y):
        return x+y
    return xxx
print(add(1)(2))


def logger(fn):
    def wapper(*args,**kwargs):
        lstart = datetime.datetime.now()
        print('arg is {}, kwargs is {}'.format(args,kwargs))
        ret = fn(*args,**kwargs)
        lstop = datetime.datetime.now()
        print('function {} tooks {}s'.format(fn.__name__,(lstop - lstart).total_seconds()))
        wapper.__name__ = fn.__name__
    return wapper
@logger
def add(x,y):
    """sdfjlslfjajdfjalsfjja1111"""
    return x+y

print(add(11,y=66),add.__name__,add.__doc__)