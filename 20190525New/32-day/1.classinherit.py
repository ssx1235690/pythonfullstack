# -*- coding: utf-8 -*-
# @Time    :  2019/11/20
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.classinherit

class A:
    __classA = 100
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

print(B.__base__)
print(B.__bases__)
print(B.__mro__)
print(B.__subclasses__)

print(A.__dict__)
print(B.__dict__)