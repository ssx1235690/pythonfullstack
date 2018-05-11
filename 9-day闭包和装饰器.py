#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/15

'''
闭包的概念就是一个内部函数+定义这个函数的环境
'''
import time
def outer():
    x = 10
    def inner():
        print(x)
    return inner
outer()()
f = outer()
f()
'''
inner的引用违反了变量的LEGB原则但是他就是可行的你不服不行，这就是闭包
'''
#简单的装饰器写法
def shijian(f):
    def inner():
        start = time.time()
        print(start)
        f()
        end = time.time()
        print(start-end)
    return  inner

@shijian #foo = shijian(foo),@会自动读取到下面匹配到的第一个函数很给力。
def foo():
    print('foo.......')
    time.sleep(1)
foo()
#能传参的装饰器写法
def shijian(f):
    def inner(*a,**b):
        start = time.time()
        f(*a,**b)
        end = time.time()
        print(end-start)
    return  inner

@shijian #foo = shijian(foo),@会自动读取到下面匹配到的第一个函数很给力。
def foo(*a,**b):
    for i in a:
        print(i,end=' ')
    time.sleep(1)
foo(1,2,3,4,5,6)

#修饰器的嵌套
def log(flag):
    def shijian(f):
        def inner(*a, **b):
            start = time.time()
            f(*a, **b)
            end = time.time()
            if flag == True:
                print(end - start)
        return inner
    return shijian
@log('False')
def foo(*a,**b):
    for i in a:
        print(i,end=' ')
    time.sleep(1)
foo(1,2,3,4,5,6)
'''
修饰器的嵌套就是制造闭包使我们的修饰器能引用外层的变量，这样我们就可以传入一个叫做flag的变量进行一个标志位判断
@log(flag)=shijian的一个闭包返回一个闭包函数shijian不说还给我们创造了一个闭包变量flag
'''

