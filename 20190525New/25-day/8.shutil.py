# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 21:48
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 8.shutil.py

import  shutil
import os

import sys


print(os.name)  # windows nt   linux   posix
# print(os.uname())#AttributeError: module 'os' has no attribute 'uname'

print(sys.platform)


####  shell  util 模块


#  copy 方法
shutil.copy('song1.txt','song2.txt')
shutil.copyfile('song1.txt','song2.txt')
shutil.copymode('song1.txt','song2.txt')
#