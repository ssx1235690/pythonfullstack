#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 15:28
# @Author  : sxsong
# @Site    : 
# @File    : 20-day协程.py
# @Software: PyCharm


################# http://www.cnblogs.com/alex3714/articles/5248247.html     #####################


import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # pass
        # time.sleep(1)


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        print("\033[32;1m[producer1]\033[0m is making baozi %s" % n)
        con.send(n)
        print("\033[32;1m[producer2]\033[0m is making baozi %s" % n)
        con2.send(n)



if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()



