# -*- coding: utf-8 -*-
# @Time    :  2020/3/17
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.class_test


_name1 = 'songle'

class zz:
    def __init__(self):
        self._name2 = _name1
    def get_song(self):
        return self._name2

print(dir())
print(dir(zz))
print(zz().get_song())