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
# print(ll)




########## getattr 对实例级别的异常进行控制

class  Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __getattr__(self, item):
        print(4,item,'------------------------------')
        print(5,type(item),'~~~~~~~~~~~~~~~~~~~~~')
        return 123456
    def __setattr__(self, key, value):
        print('setattr',key,value)
        # self.key = value 会引起递归循环
        self.__dict__[key] = value
        # pass return NONE



p = Point(4,5)
print(1,p)
print(2,p.x,p.y)
print(3,p.n)



### 如果实例中存在相应属性那么不会引起 getattr 属性调用， 使用 dict 方式进行赋值不会调用setaatr 方法

print(p.yy)
p.__dict__['yy']  = 1000

print(p.zz)
p.zz = 100000
print(p.zz)



### getatribute()---instance dict ----- class dict --- 父类 dict ---- getattr（）


class  Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __getattr__(self, item):
        print(4,item,'------------------------------')
        print(5,type(item),'~~~~~~~~~~~~~~~~~~~~~')
        return 123456
    def __setattr__(self, key, value):
        print('setattr',key,value)
        # self.key = value 会引起递归循环
        print(type(self),self.__dict__,'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        self.__dict__[key] = value
        # pass return NONE
    def __getattribute__(self, item):
        return {}

song = Point('zz','yy')
