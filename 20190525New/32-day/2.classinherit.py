# -*- coding: utf-8 -*-
# @Time    :  2019/11/24
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.classinherit


class A():
    a = 10
    def __init__(self,a):
        self.a = a
        # return self.a

class B(A):
    def __init__(self,b,c):
        self.b = b
        self.c  = c
        super().__init__(10000)
        # A.__init__(self,10000000)

    def printall(self):
        print(self.a)

b = B(4,5)
b.printall()

