#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 15:33
# @Author  : sxsong
# @Site    : 
# @File    : 24-dayMysql分页.py
# @Software: PyCharm


# 每页显示10条：
# 当前 118 120， 125
#
# 倒序：
#             大      小
#             980    970  7 6  6 5  54  43  32
#
# 21 19 98
# 下一页：
#
#     select
#         *
#     from
#         tb1
#     where
#         nid < (select nid from (select nid from tb1 where nid < 当前页最小值 order by nid desc limit 每页数据 *【页码-当前页】) A order by A.nid asc limit 1)
#     order by
#         nid desc
#     limit 10;
#
#
#
#     select
#         *
#     from
#         tb1
#     where
#         nid < (select nid from (select nid from tb1 where nid < 970  order by nid desc limit 40) A order by A.nid asc limit 1)
#     order by
#         nid desc
#     limit 10;
#
#
# 上一页：
#
#     select
#         *
#     from
#         tb1
#     where
#         nid < (select nid from (select nid from tb1 where nid > 当前页最大值 order by nid asc limit 每页数据 *【当前页-页码】) A order by A.nid asc limit 1)
#     order by
#         nid desc
#     limit 10;
#
#
#     select
#         *
#     from
#         tb1
#     where
#         nid < (select nid from (select nid from tb1 where nid > 980 order by nid asc limit 20) A order by A.nid desc limit 1)
#     order by
#         nid desc
#     limit 10;