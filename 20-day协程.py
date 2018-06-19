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


'''
看楼上的例子，我问你这算不算做是协程呢？你说，我他妈哪知道呀，你前面说了一堆废话，但是并没告诉我协程的标准形态呀
，我腚眼一想，觉得你说也对，那好，我们先给协程一个标准定义，即符合什么条件就能称之为协程：
必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
一个协程遇到IO操作自动切换到其它协程
基于上面这4点定义，我们刚才用yield实现的程并不能算是合格的线程，因为它有一点功能没实现，哪一点呢？
'''
