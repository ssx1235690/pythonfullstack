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
    def __init__(self):
        print(self._xxx)
        try:
            print(super().__xxx2)
        except BaseException as e:
            print(e)


l1 = song()
l2 = lele()
