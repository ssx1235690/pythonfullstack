#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/18

#########迭代器的一个子集就是生成器
###迭代器是由可迭代对象调用调用对象函数__iter__()或者直接使用内置的函数iter（）来生成的
l = [1,2,3,4]
l.__iter__()
iter(l)

#迭代器都可以使用一个 next（），生成器都是迭代器所以它也可以使用 next（）
'''
迭代器

我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
1
2
3
4
5
6
7
8
9
10
11
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
'''
'''
小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
'''
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break