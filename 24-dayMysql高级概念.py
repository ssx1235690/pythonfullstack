#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 10:52
# @Author  : sxsong
# @Site    : 
# @File    : 24-dayMysql高级概念.py
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