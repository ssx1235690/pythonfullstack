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