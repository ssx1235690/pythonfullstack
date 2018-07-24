#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 18:49
# @Author  : sxsong
# @Site    : 
# @File    : 24-dayMysql高级概念索引和方法.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="song")
cursor = conn.cursor()
cursor.execute('select * from student where  sid=1')
song=cursor.fetchall()
print(song)
conn.close()



########################## 1、自定义函数######################################

# 复制代码
# delimiter \\
# create function f1(
#     i1 int,
#     i2 int)
# returns int
# BEGIN
#     declare num int;
#     set num = i1 + i2;
#     return(num);
# END \\
# delimiter ;
#
# 函数和存储过程的不同
# 1.函数可以定义返回值 ，存储过程不可以一定要通过 in out 来辅助
# 2.函数中不可以有sql

###############################删除函数############################################
# drop function func_name;

##############################执行函数#######################################
# 获取返回值
# declare @i VARCHAR(32);
# select UPPER('alex') into @i;
# SELECT @i;
#
#
# # 在查询中使用
# select f1(11,nid) ,name from tb2;