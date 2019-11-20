# -*- coding: utf-8 -*-
# @Time    :  2019/11/10
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.practise_class


class Animal():
    _xx1  = 22
    __xxx2 = 222
    def __init__(self):
        self._xx3 = 33
        self.__xxx3 = 333

cat = Animal()
print(Animal.__dict__)
print(cat.__dict__)