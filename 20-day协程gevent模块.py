#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 19:10
# @Author  : sxsong
# @Site    : 
# @File    : 20-day协程gevent模块.py
# @Software: PyCharm

import gevent
import  time
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()



def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(0.1)
    # time.sleep(1)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(0.09)
    # time.sleep(0.09)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])

from gevent import monkey;

monkey.patch_all()
import gevent
from  urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])