# -*- coding: utf-8 -*-
# @Time    :  2020/6/21
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : reflection

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return self.x,self.y
    def show(self):
        print(self.x,self.y)

a = A(3,5)
print(A.__dict__)
print(a.__dict__)
print(dir(a))
print(a.__dir__())

# 通过修改实例字典，进行属性修改

setattr(a,'x','tadayima')
print(a.__dict__)

print(hasattr(a,'x'))

import functools
# print(functools.__dict__)

setattr(functools,'lele','niubi')
ll = getattr(functools,'lele')
print(ll)