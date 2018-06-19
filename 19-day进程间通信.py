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

# from multiprocessing import Process,Pipe
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn,child_conn = Pipe()
#     print(child_conn)
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # prints "[42, None, 'hello']"
#     p.join()



############################### Manager ############################################
from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print('sub',id(d))
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        print('main',id(d))
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)
