# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 19:25
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.返回值.py


# return 相当于 break 对于循环的控制。直接使本函数出栈。不再执行


def song():
    return 1,2,3
x,y,z = song()
print(x,y,z)

def song():
    return (1,)
ll = song()
print(type(ll))




#### 函数嵌套


def song():
    def lele():
        print('song lele is a lovely boy')
    lele()

song()