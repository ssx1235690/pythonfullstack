#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/5/10

import  threading
import  time
print('start')

def song(bar):
    time.sleep(1)
    print('song',bar)
def xiang(bar):
    time.sleep(2)
    print('xiang',bar)

t1 = threading.Thread(target=song,args=('lele',))
t2 = threading.Thread(target=xiang,args=('baba',))

t1.start()
t2.start()


# t1.join()
#
# t2.join()


print(time.time())


##############################间接调用##########################
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

