#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:15
# @Author  : sxsong
# @Site    : 
# @File    : 24-dayMysql高级概念触发器.py
# @Software: PyCharm



######################################## 触发器 ##############################################
# 对某个表进行【增/删/改】操作的前后如果希望触发某个特定的行为时，可以使用触发器，触发器用于定制用户对表的行进行【增/删/改】前后的行为。
#
# 1、创建基本语法

# 复制代码
# # 插入前
# CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END
#
# # 插入后
# CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END
#
# # 删除前
# CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END
#
# # 删除后
# CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END
#
# # 更新前
# CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END
#
# # 更新后
# CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
# BEGIN
#     ...
# END