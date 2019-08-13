# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0:06
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.pickle.py

import pickle

song = 'a'
with open('song.txt','wb') as xxx:
    xxx.write(pickle.dumps(song))


class song():
    def __init__(self):
        self.son = 'lele'
        self.name = 'xiang'
    def sing(self):
        return self.name + self.son

with open('song.txt','wb+') as xxx:
    xxx.write(pickle.dumps(song()))



print(pickle.DEFAULT_PROTOCOL)
class Foo(str):
    attr = 'A class attribute'
    print(123)
    def xxx(self):
        self.xxxxx = 123
    def ok(self):
        print(self.xxxxx)

picklestring = pickle.dumps(Foo())


print(picklestring)