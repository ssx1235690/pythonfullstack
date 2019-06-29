# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 20:41
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 4.nonlocal和defult.py

x = 100

#### nonlocal 不能代替 global 不能做以下替代

# def outer():
#     nonlocal x
#     x =  100
#     def inner():
#         nonlocal x
#         print(x)
#     return inner
# ll = outer()
# ll()


############# 下面还有一个有趣的例子 带我们 认识  defaults  这样的变量


def outer(xyz=[],zz=1):
    xyz.append(100)
    zz += 1
    print(xyz)
    print(zz)
outer()
outer()
outer()
print(outer.__defaults__)

def outer(xyz=1):
    xyz += 1
    print(xyz)
outer()
outer()
outer()
print(outer.__defaults__)

######## 使用 下列两种方式 避免这个问题

def outer(xyz=[],zz=1):
    xyz = xyz[:]  # 拷贝一份
    xyz.append(100)
    zz += 1
    print(xyz)
    print(zz)
outer()
outer()
outer()
print(outer.__defaults__)



def outer(xyz=None,zz=1):
    if xyz == None:
        xyz = []
    xyz.append(100)
    zz += 1
    print(xyz)
    print(zz)
outer()
outer()
outer()
print(outer.__defaults__)



x = [1,2,3]
print(x[:])