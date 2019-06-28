# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 23:50
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.datetime.py

import datetime

print(datetime.time())
# 以 年 月 日 时 分 秒 微米 来计时
print(datetime.datetime(2019,6,28,20,45,23,1223))

# weekday()  计算时间对象时星期几
ll = datetime.datetime(2019,6,28,20,45,23,1223)
print(ll.weekday())
print(ll.isoweekday())

#
print(datetime.date(2019,6,28))



# date str 方法

df = datetime.datetime.strptime('2019-06-25  20:08',"%Y-%m-%d  %H:%M")
print(df)

# 以下两种方式等价

print(df.strftime("%Y-%m-%d  %H:%M"))
print("{0:%Y}-{0:%m}-{0:%d}  {0:%H}:{0:%M}".format(df))



import time


time.sleep(5)

