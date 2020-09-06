# -*- coding: utf-8 -*-
# @Time    :  2020/9/6
# @Author  :  user01
# @Email   : ......998@qq.com
# @File    : 2.描述器

#
# 描述器的三个魔术方法
#
# object.__set__(self,instance,value)
# object.__get__(self,instance,owner)
# object.__delete__(self,instance)


class A:
    def __init__(self,f):
        self.f = f
        print('init A ')
    def __get__(self, instance, owner):
        print(self,instance,owner)
    def __set__(self, instance, value):
        print(self,instance,value)

class B:
    f = A(1)
    def __init__(self):
        print('init B')

print(B.f)

b = B()

print(b.f)