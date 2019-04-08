# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 14:58
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.class.py

from os import system
import json

class song():
    _xxx = 123
    __xxx2 = 1234

    def __init__(self):
        self.name= self._xxx
        print(self.__xxx2)
        print(self.name)

class lele(song):
    xxxxx='123cccc'
    def __init__(self):
        print(self._xxx)
        try:
            self.sss()
            print(super()._xxx2)
        except BaseException as e:
            print(e)
    @staticmethod # 名义上归类来管理
    def fun1_static():
        print('static')
    @classmethod   #类方法只能访问类变量，不能访问实例变量
    def fun2_class(cls):
        print(cls.xxxxx)
    @property         #把一个方法变成一个静态属性
    def  fun3_propp(self):
        print('xxxx',self.__propp_song)
    @fun3_propp.setter
    def propp(self,arg1):
        print(song)
        self.__propp_song = arg1




l1 = song()
l2 = lele()
l2.propp='kjhkjhjkhj'
l2.fun3_propp


print('''
# 特殊的类变量
''')


# print(dir(system))
class Base(object):
    def test(self):
        print()


class A(Base):
    def test(self):
        print("------------A")


class B(Base):
    def test(self):
        print("------------B")


class C(A, B):
    pass
    # def test(self):
    #    print("------------C")


c = C()
c.test()
print(C.__mro__)
