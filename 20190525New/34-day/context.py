# -*- coding: utf-8 -*-
# @Time    :  2020/5/22
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : context


class A:
    def __enter__(self):
        print('enter')

    def __str__(self):
        return 'context class test'

    def __repr__(self):
        return 'class context print function'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

with A() as a:
    print(a)
    '''
    context class test
    <class 'NoneType'>
    '''
    print(A())
    print(type(a))
# 因为 A() 返回 none 所以 as 子句只能获取 none ， 在enter 中定义 reture 加以解决


import datetime

from functools import update_wrapper,wraps

class Time:
    '''this is in class'''
    def __init__(self,fn,output = lambda fn,detal : print('方法{} 花费时间为{}'.format(fn,detal))):
        self.output = output
        self.fn = fn
        update_wrapper(self,fn)
        # wraps(fn)(self)

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.detal = (datetime.datetime.now() - self.start).total_seconds()
        return self.detal

    def __call__(self,x,y):
        self.start = datetime.datetime.now()
        self.detal = (datetime.datetime.now() - self.start).total_seconds()
        self.output(self.fn,self.detal)
        return self.fn(x,y)

@Time
def add(x,y):
    '''this is a function'''
    print(x+y)

add(5,6)
print(add.__doc__)

#覆盖了原函数的部分属性  要使用 wrapper 函数进行二次修饰

