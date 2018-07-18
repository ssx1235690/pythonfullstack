#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 15:11
# @Author  : sxsong
# @Site    : 
# @File    : 23-dayMySql-3.py
# @Software: PyCharm



import  pymysql
import logging


# http://www.cnblogs.com/wupeiqi/articles/5713330.html

# # 创建连接
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# # 创建游标
# cursor = conn.cursor()
#
# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
#
# # 执行SQL，并返回受影响行数
# # effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
#
# # 执行SQL，并返回受影响行数
# # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
#
#
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()



logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y/%m/%d %H:%M:%S',filename=r'c:\users\ronglian\desktop\mylog.txt', filemode='a')

conn = pymysql.connect(host="localhost",user="root",password="",db="song",charset='utf8')
cursor = conn.cursor()
print(cursor)
cursor.execute('select * from teacher')
song = cursor.fetchall()
print(song)
print(type(song))
try:
    cursor.execute('insert into teacher (tid,tname) VALUE (7,"宋妖妖老师")')
    conn.commit()
except Exception as song:
    logging.error(song)
    conn.close()

new_id = cursor.lastrowid
print(new_id)