# -*- coding: utf-8 -*-
# @Time    :  2020/3/18
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.运算符


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self):
        self.c = MyClass.i

    def f(self):
        return 'hello world'
    def __bool__(self):
        # return False
        return True

print(dir(MyClass()))


a = 100

def song():
    a = 100000

    def song2():
        nonlocal  a
        a = 1000
    song2()
song()
print(dir(song))