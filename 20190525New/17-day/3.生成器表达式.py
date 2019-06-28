# -*- coding: utf-8 -*-
# @Time    :  2019/6/28 21:57
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.生成器表达式.py

### 表达式 为 （返回值  for 表达式）  返回一个生成器


song = (x for x in range(5))

#### 可迭代对象  >   迭代器  因为生成器 字符串  列表  也是可迭代对象。  判断是否为迭代器的方法为next

def lele(x):
    for i in range(x):
        yield
        return i
# print(type(lele(10)))
# lele(10).next()
# AttributeError: 'generator' object has no attribute 'next'

song = iter(lele(10))  # 转换方法
song.__next__()


##################### 迭代器 有指针概念 不能重复迭代

song=  (x for x in range(2))
first = next(song)
second = next(song)
total = first + second
# print(next(song))
#
# Traceback (most recent call last):
#   File "D:/PycharmProjects/pythonfullstack/20190525New/17-day/3.生成器表达式.py", line 32, in <module>
#     print(next(song))
# StopIteration