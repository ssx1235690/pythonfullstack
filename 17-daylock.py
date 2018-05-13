#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/5/11

import threading,time
num = 100

r = threading.Lock()

def fun():
    global num

    ###### 不加锁
    # num -= 1

    r.acquire()
    tmp = num
    time.sleep(0.00001)
    tmp -= 1
    num = tmp
    r.release()


thread_llist = []

for i in range(100):
    t = threading.Thread(target=fun)
    t.start()
    thread_llist.append(t)
for i in thread_llist:
    t.join()

print(num)

