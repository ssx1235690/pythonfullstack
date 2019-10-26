# -*- coding: utf-8 -*-
# @Time    :  2019/10/26
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : class_method

class Person():

    def song(a1):   # 此处的 al  ===  self  代表实例
        print(a1)

    def song2(a2):
        a2.name = 'a2 in song2'
    @classmethod
    def xxx(cls):
        print('xcvvc')
        print(type(cls))
        print(cls.__dict__.items())

    @staticmethod
    def xxx2():   #解决了传入变量数量的问题
        print('name in xxx2')

### class method 使用类直接调用的方法
Person.song('sdfsfsfds')

#     Person().song('sdfsfsfds')
# TypeError: song() takes 1 positional argument but 2 were given
# Person().song('sdfsfsfds')
Person().xxx()
ll = Person()
print(ll.song2())
print(ll.name)
ll.xxx()