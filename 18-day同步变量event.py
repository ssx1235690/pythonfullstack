#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/5/13

# 同步条件(Event)
#       条件同步和条件变量同步差不多意思，只是少了锁功能，因为条件同步设计于不访问共享资源的条件环境。event=threading.Event()：条件环境对象，初始值 为False；
#
# 复制代码
# event.isSet()：返回event的状态值；
#
# event.wait()：如果 event.isSet()==False将阻塞线程；
#
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
#
# event.clear()：恢复event的状态值为False。

import threading,time
class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        event.isSet() or event.set()
        time.sleep(1)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set()
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(0.25)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")
if __name__=="__main__":
    event=threading.Event()
    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()



# 红绿灯实例
import random
def light():
    if not event.isSet():
        event.set() #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()