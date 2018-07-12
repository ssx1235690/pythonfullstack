#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 15:56
# @Author  : sxsong
# @Site    : 
# @File    : 23-dayMySql-1.py
# @Software: PyCharm

import  pymysql

# MySql1

# http://www.cnblogs.com/wupeiqi/articles/5713315.html

# MySql2
# http://www.cnblogs.com/wupeiqi/articles/5713323.html

# MySql3
# http://www.cnblogs.com/wupeiqi/articles/5729934.html


MysqlHost = "192.168.33.100"


# Mysql window anzhuang



##############################3# 一、概述 #######################################################
# 1、什么是数据库 ？
# 　答：数据的仓库，如：在ATM的示例中我们创建了一个 db 目录，称其为数据库
#
# 2、什么是 MySQL、Oracle、SQLite、Access、MS SQL Server等 ？
# 　答：他们均是一个软件，都有两个主要的功能：
#
# a. 将数据保存到文件或内存
# b. 接收特定的命令，然后对文件进行相应的操作
#
# PS：如果有了以上软件，无须自己再去创建文件和文件夹，而是直接传递 命令 给上述软件，让其来进行文件操作，他们统称为数据库管理系统（DBMS，Database Management System）
# 3、什么是SQL ？
# 　答：上述提到MySQL等软件可以接受命令，并做出相应的操作，由于命令中可以包含删除文件、获取文件内容等众多操作，
# 对于编写的命令就是是SQL语句。SQL􏰉􏵮􏵯􏰟，是􏵱􏰚􏵲􏵳􏵴􏰇􏰈􏵱􏰚􏵲􏵳􏵴􏰇􏰈结构化语言（Structured Query Language􏰕􏰐􏵵􏰯）的缩写，SQL􏰜􏰖􏰩􏰽􏵶􏱥􏲲􏰄􏰫􏰬􏰭􏵁􏵷􏰐􏰇􏰈是一种专门用来与数据库通信的语言。


conn = pymysql()