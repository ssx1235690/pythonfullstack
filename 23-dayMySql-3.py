#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 15:11
# @Author  : sxsong
# @Site    : 
# @File    : 23-dayMySql-3.py
# @Software: PyCharm

# http://www.cnblogs.com/wupeiqi/articles/5713330.html


import  pymysql
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y/%m/%d %H:%M:%S',filename=r'c:\users\ronglian\desktop\mylog.txt', filemode='a')

conn = pymysql.connect(host="localhost",user="root",password="",db="song",charset='utf8')
cursor = conn.cursor()
print(cursor)
cursor.execute('select * from teacher')
song = cursor.fetchall()
print(song)
print(type(song))
try:
    cursor.execute('insert into teacher (tid,tname) VALUE (6,"宋逍遥老师")')
    conn.commit()
except Exception as song:
    logging.info(song)
    conn.close()


