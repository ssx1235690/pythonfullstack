#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/5/10

import time
import threading

start_time = time.time()

def add(n):
    sum = 0
    for i in range(n):
        sum += n
    print(sum)


add(80000000)
add(160000000)
# 8.688497066497803

# t1 = threading.Thread(target=add,args=(80000000,))
# t2 = threading.Thread(target=add,args=(160000000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# 8.857506513595581

stop_time = time.time()

print(stop_time - start_time)





import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print ("Begin listening to %s. %s" %(func,ctime()))
        sleep(4)
        print("end listening %s"%ctime())

def move(func):
    for i in range(2):
        print ("Begin watching at the %s! %s" %(func,ctime()))
        sleep(5)
        print('end watching %s'%ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        # t.setDaemon(True)
        t.start()
        # t.join()
    # t1.join()
    t2.join()########考虑这三种join位置下的结果？
    print ("all over %s" %ctime())


# setDaemon(True)：
#
#       将线程声明为守护线程，必须在start() 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。这个方法基本和join是相反
    # 的。当我们 在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程
    # 完成想退出时，会检验子线程是否完成。如 果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是
    # 只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦
#
# join()：
#
#        在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
#
# 其它方法
#
#
# 复制代码
# thread 模块提供的其他方法：
# # threading.currentThread(): 返回当前的线程变量。
# # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# # 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# # run(): 用以表示线程活动的方法。
# # start():启动线程活动。
# # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# # isAlive(): 返回线程是否活动的。
# # getName(): 返回线程名。
# # setName(): 设置线程名。