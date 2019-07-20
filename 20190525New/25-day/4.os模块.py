
# -*- coding: utf-8 -*-
# @Time    :  2019/7/19 11:03
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.os模块.py

from os import path


p = path.join('D:/','svn','ResourceManage','00密码管理')

p = path.abspath(__file__)

print(p,type(p))

print(path.exists(p))
print(path.abspath(p))

print(path.split(path.abspath(p)))

print(path.dirname(path.abspath(p)))
print(path.basename(path.abspath(p)))


