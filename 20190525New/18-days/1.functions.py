# -*- coding: utf-8 -*-
# @Time    :  2019/6/28 22:34
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.functions.py

### 函数传参的错误点


def song(x,y):
    pass

song(1,2)
song(1,y=2)

# song(x=5,4)
# SyntaxError: positional argument follows keyword argument

def song(x=1,y=3):
    pass

song(1,2)
song(1,y=2)

song(x=5,4)
# SyntaxError: positional argument follows keyword argument

# song(3,x=5)
#
# TypeError: song() got multiple values for argument 'x'