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
# 但是可以执行动态赋值
# declare  a int;
# set  a = 123
# select sdf into a from tb1  where xxxxxxxxxxx

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



#################################################################################################################
############################################ 索引  ###############################################################
# 索引，是数据库中专门用于帮助用户快速查询数据的一种数据结构。类似于字典中的目录，查找字典内容时可以根据目录查找到数据的存放位置，然后直接获取即可。

# MySQL中常见索引有：
#
# 普通索引
# 唯一索引
# 主键索引
# 组合索引
# 1、普通索引
#
# 普通索引仅有一个功能：加速查询
#
#
# 复制代码
# 增删改查
# create table in1(
#     nid int not null auto_increment primary key,
#     name varchar(32) not null,
#     email varchar(64) not null,
#     extra text,
#     index ix_name (name)
# )

# create index index_name on table_name(column_name)

# drop index_name on table_name;

# show index from table_name;


# 2、唯一索引
#
# 唯一索引有两个功能：加速查询 和 唯一约束（可含null）
#
# 增删改查
# 复制代码
# create table in1(
#     nid int not null auto_increment primary key,
#     name varchar(32) not null,
#     email varchar(64) not null,
#     extra text,
#     unique ix_name (name)
# )
# 复制代码
#
# create unique index 索引名 on 表名(列名)
#
# drop unique index 索引名 on 表名



# 3、主键索引
#
# 主键有两个功能：加速查询 和 唯一约束（不可含null）
#
#
# 增删改查
# create table in1(
#     nid int not null auto_increment primary key,
#     name varchar(32) not null,
#     email varchar(64) not null,
#     extra text,
#     index ix_name (name)
# )
#
# OR
#
# create table in1(
#     nid int not null auto_increment,
#     name varchar(32) not null,
#     email varchar(64) not null,
#     extra text,
#     primary key(ni1),
#     index ix_name (name)
# )
# 复制代码
#
# alter table 表名 add primary key(列名);
#
# alter table 表名 drop primary key;
# alter table 表名  modify  列名 int, drop primary key;



# 4、组合索引
#
# 组合索引是将n个列组合成一个索引
#
# 其应用场景为：频繁的同时使用n列来进行查询，如：where n1 = 'alex' and n2 = 666。
#
#
# 复制代码
# create table in3(
#     nid int not null auto_increment primary key,
#     name varchar(32) not null,
#     email varchar(64) not null,
#     extra text
# )
# 复制代码
#
# create index ix_name_email on in3(name,email);
# 如上创建组合索引之后，查询：
#
# name and email  -- 使用索引
# name                 -- 使用索引
# email                 -- 不使用索引
# 注意：对于同时搜索n个条件时，组合索引的性能好于多个单一索引合并。


# 1、覆盖索引
#
#         select * from tb where nid=1
#         # 先去索引中找，
#         # 在去数据表找
#
#         select nid from tb where nid < 10
#         # 先去索引中找
#
#         -- 情况应用上索引，并且不用去数据表中操作，覆盖索引0
#         -- 只需要在索引表中就能获取到数据时，
#     2、合并索引
#         nid   name(单独索引)    email（单独索引）    pwd
#
#         select * from tb where name='alex'
#         select * from tb where email='alex3714@163.com'
#
#         select * from tb where name='alex' or email='alex3714@163.com'
#
#
#
#         nid   name(组)    email（合）    pwd
#         # 最左前缀
#
#         select * from tb where name='alex'
#         select * from tb where email='alex3714@163.com' ########无法满足########
#
#         select * from tb where name='alex' or email='alex3714@163.com'
#
#
#
#        用户表：
#             nid   username（组）    password（合）
#              1     alex         123
#              2     shaogbing    123
#
#
#             select * from tb where username='xx' and password='xx'
#             select * from tb where username='xx'
#             # select * from tb where password='xx'
#
#             --> 组合和合并索引取舍？业务需求来决定
#
#
#     3、执行计划 - 相对比较准确表达出当前SQL运行状况
#
#
#         是否走索引，不走索引
#
#         explain SQL语句
#
#
#         1、explain SQL语句
#             type： ALL    - 全数据表扫描
#             type： index  - 全索引表扫面
#
#         2、limit
#             select * from tb1 where email='123'
#
#             select * from tb1 where email='123' limit 1;
#
#         -----SQL： ALL、Index，都是有优化的余地 -------
#
#     4、如何命中索引
#
#
#         nid name          ctime
#                      2016-9-10 11:59
#
#
#
#         当前时间：
#
#                                       2016/9/10
#         select * from tb1 where conv(ctime,'.,..') = time;
#         # 转船
#         select * from tb1 where ctime = 转(2016/9/10)=> 2016-9-10
#
#     5、分页
#
#         limit x,m :  表x+m
#
#         where nid>10000 直接跳过 钱10000条数，继续往下扫
#
#         每页：10条
#         1     2    3     4  ...    18  19  20  21
#         1     17   31   45
#         16    29   42   90
#
#         -- nid排列可能中断的
#
#         ---------- 方式： 上一页下一页 ----------
#
#         1、当用查看页面时，第一页 limit 0,10： nid: 1 - 16
#
#
#         2、第一页 limit 10,10： nid: 17 - 36
#         3、第一页 limit 100000,10： nid: 17 - 36
#
#
#         2、第一页 where nid>16 limit 10： nid: 17 - 36
#         3、第一页 where nid>36 limit 10： nid: 170 - 360
#     6、慢SQL日志
#     6、慢SQL日志
