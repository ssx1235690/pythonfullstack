#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 15:11
# @Author  : sxsong
# @Site    : 
# @File    : 23-dayMySql-3.py
# @Software: PyCharm


import  pymysql
import logging


conn = pymysql.connect(host="localhost",user="root",password="",db="song",charset='utf8')
cursor = conn.cursor()
print(cursor)
cursor.execute('select * from teacher')
song = cursor.fetchall()
print(song)
print(type(song))
try:
    cursor.execute('insert into teaches (tid,tname) VALUE (6,"宋逍遥老师")')
    cursor.commit()
except Exception as song:

conn.close()