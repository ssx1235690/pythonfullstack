#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 17:48
# @Author  : sxsong
# @Site    : 
# @File    : 19-day进程间通信.py
# @Software: PyCharm

#######################Queue 方式 ########################################
# from multiprocessing import Process, Queue
# import queue
# def f(q,n):
#     q.put([42, n, 'hello'])
#     print(id(q))
#
# if __name__ == '__main__':
#     q = Queue()
#     # q = queue.Queue()
# ################### 使用线程queue的时候会造成没有办法反序列化的过程
#     #################TypeError: can't pickle _thread.lock objects
#
#     p_list=[]
#     print(id(q))
#     for i in range(3):
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#             i.join()



############################ Pipe 模式##########################################

from multiprocessing import Process,Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    print(child_conn)
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()


