#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 10:52
# @Author  : sxsong
# @Site    : 
# @File    : 24-dayMysql高级概念视图和过程.py
# @Software: PyCharm


# http://www.cnblogs.com/wupeiqi/articles/5713323.html

###############视图的概念###############################
# 视图是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，并可以将其当作表来使用。

# 1、创建视图##########################################################
#
#
# 复制代码
# --格式：CREATE VIEW 视图名称 AS  SQL语句
# CREATE VIEW v1 AS
# SELET nid,
#     name
# FROM
#     A
# WHERE
#     nid > 4

# 2、删除视图###############################################################

# --格式：DROP VIEW 视图名称

# DROP VIEW v1



# 3、修改视图


# 复制代码
# -- 格式：ALTER VIEW 视图名称 AS SQL语句
#
# ALTER VIEW v1 AS
# SELET A.nid,
#     B. NAME
# FROM
#     A
# LEFT JOIN B ON A.id = B.nid
# LEFT JOIN C ON A.id = C.nid
# WHERE
#     A.id > 2
# AND C.nid < 5

# 4、使用视图
#
# 使用视图时，将其当作表进行操作即可，由于视图是虚拟表，所以无法使用其对真实表进行创建、更新和删除操作，仅能做查询用。
#
#
# select * from v1



######################################存储过程######################################################
# 存储过程是一个SQL语句集合，当主动去调用存储过程时，其中内部的SQL语句会按照逻辑执行。
#
# 1、创建存储过程
#
#
# 复制代码
# -- 创建存储过程
#
# delimiter //
# create procedure p1()
# BEGIN
#     select * from t1;
# END//
# delimiter ;
#
#
#
# -- 执行存储过程
#
# call p1()


# 对于存储过程，可以接收参数，其参数有三类：
#
# in          仅用于传入参数用
# out        仅用于返回值用
# inout     既可以传入又可以当作返回值
#
# 复制代码
# -- 创建存储过程
# delimiter \\
# create procedure p1(
#     in i1 int,
#     in i2 int,
#     inout i3 int,
#     out r1 int
# )
# BEGIN
#     DECLARE temp1 int;
#     DECLARE temp2 int default 0;
#
#     set temp1 = 1;
#
#     set r1 = i1 + i2 + temp1 + temp2;
#
#     set i3 = i3 + 100;
#
# end\\
# delimiter ;
#
# -- 执行存储过程
# set @t1 =4;
# set @t2 = 0;
# CALL p1 (1, 2 ,@t1, @t2);
# SELECT @t1,@t2;

#
# 2、删除存储过程######################################################
#
#
# drop procedure proc_name;
# 3、执行存储过程########################################################
#
#  执行存储过程
#
# 复制代码
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# # 执行存储过程
# cursor.callproc('p1', args=(1, 22, 3, 4))
# # 获取执行完存储的参数
# cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
# result = cursor.fetchall()
#
# conn.commit()
# cursor.close()
# conn.close()
#
#
# print(result)


#####自己练习
# 过程添加
# delimiter \\
# create procedure p1(
#     in i1 int,
#     in i2 int,
#     inout i3 int,
#     out r1 int
# )
# BEGIN
#     DECLARE temp1 int;
#     DECLARE temp2 int default 0;
#
#     set temp1 = 1;
#
#     set r1 = i1 + i2 + temp1 + temp2;
#
#     set i3 = i3 + 100;
#
# end\\
# delimiter ;
import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="song")

cursor = conn.cursor()
cursor.execute('select * from students')
song = cursor.fetchall()
print(song)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.callproc('p1',args=(1,22,33,44))
cursor.execute('select @_p1_0,@_p1_1,@_p1_2,@_p1_3')
song =cursor.fetchall()
print(song)
print(song[0].values())
conn.close()


