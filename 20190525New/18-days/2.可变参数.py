# -*- coding: utf-8 -*-
# @Time    :  2019/6/28 22:46
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.可变参数.py


def song(*x,**y):
    print(x)
    print(y)

song(1,2,3,4,5,b=8,c=8)
# song(b=8,c=8,1,2,3,4,5)
# SyntaxError: positional argument follows keyword argument

# 参数的位置 总结为   普通参数  > 可变位置参数 *x  > 可变关键字参数  **y


#
# def song(**sss,x):
#     pass
#
#     def song(**sss,x):
#                    ^
# SyntaxError: invalid syntax