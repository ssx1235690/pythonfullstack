# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 14:58
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.class.py


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
        print('xxxx',self.propp_song)
    @fun3_propp.setter
    def propp_setter(self,song):
        print(song)
        self.propp_song = song




l1 = song()
l2 = lele()
l2.propp_setter='sdfsdfsdfs'
l2.fun3_propp


