#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/18
import time
import random

#print(help(time))
'''
Functions:
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone
'''
print(time.time())
print(time.clock())
print(time.gmtime())#打印的UTC时间和我们的CST时间相差8个小时
print(time.localtime())#打印的我们的CST时间
print(time.asctime())
print(time.ctime())


####g格式化输出
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(t)
print(time.gmtime(t))
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

print('###############random###################')
# random
print(random.random())
print(random.randrange(1,3))#不包含右侧
print(random.randint(1,3))  #包含右侧
print(random.choice([1,5,7,[1,'a','ss']])) #从列表中随机选择一个
print(random.sample([1,5,7,[1,'a','ss']],2))   #从列表中选出指定数目的值
print(random.shuffle([1,5,7,[1,'a','ss']]))


print(help(random.shuffle))