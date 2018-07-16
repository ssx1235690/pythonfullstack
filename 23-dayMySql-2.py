#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 11:17
# @Author  : sxsong
# @Site    : 
# @File    : 23-dayMySql-2.py
# @Software: PyCharm


import pymysql
import os,time
from PIL import Image

# 习题  http://www.cnblogs.com/wupeiqi/articles/5748496.html
song = os.getcwd()
im = Image.open(song+r'\picture\23-day表.png')
im.show()
print('\n')
