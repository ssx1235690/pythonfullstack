# -*- coding: utf-8 -*-
# @Time    :  2020/5/22
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : context


class A:
    def __enter__(self):
        print('enter')

    def __str__(self):
        return 'context class test'

    def __repr__(self):
        return 'class context print function'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

with A() as a:
    print(a)
    '''
    context class test
    <class 'NoneType'>
    '''
    print(A())
    print(type(a))
# 因为 A() 返回 none 所以 as 子句只能获取 none ， 在enter 中定义 reture 加以解决