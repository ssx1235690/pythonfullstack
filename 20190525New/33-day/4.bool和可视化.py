# -*- coding: utf-8 -*-
# @Time    :  2020/3/17
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.bool和可视化


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self,a,b):
        self.c = a+b

    def f(self):
        return 'hello world'
    def __bool__(self):
        # return False
        return False


print(dir(MyClass))

if MyClass(1,2):
    print('bool  is  ok')