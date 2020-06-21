# -*- coding: utf-8 -*-
# @Time    :  2020/6/21
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : callfunc



def A():
    print('A call')

A()
A.__call__()

class AB:
    @classmethod
    def __call__(cls, *args, **kwargs):
        print('init')
AB()()