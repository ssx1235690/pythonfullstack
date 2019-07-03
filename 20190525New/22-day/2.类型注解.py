# -*- coding: utf-8 -*-
# @Time    :  2019/7/3 15:44
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.类型注解.py


def add(x:int,y:int):
    """
    :param x:
    :param y:
    :return:
    """
    return x + y

print(help(add))
print(add(1,2))
print(add.__annotations__)
print(add.__annotations__['x'])