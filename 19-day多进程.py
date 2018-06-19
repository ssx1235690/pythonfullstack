#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/6/13

# http://www.cnblogs.com/yuanchenqi/articles/5745958.html

# # 直接调用
# from multiprocessing import Process
# import time
# def f(name):
#     time.sleep(1)
#     print('hello', name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(15):
#         p = Process(target=f, args=('alvin',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         # p.join()
#         pass
#     print('end')
#





# # 类调用
# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess, self).__init__()
#         self.name = name
#     def run(self):
#         time.sleep(2)
#         print('hello',self.name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess('lele')
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('end')


###########小实例

# from multiprocessing import Process
# import os
# import time
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
#
# def f(name):
#     info('\033[31;1mfunction f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     time.sleep(100)
#     p = Process(target=info, args=('bob',))
#     p.start()
#     p.join()




############################################二 Process类################################
# 构造方法：
#
# Process([group [, target [, name [, args [, kwargs]]]]])
#
# 　　group: 线程组，目前还没有实现，库引用中提示必须是None；
# 　　target: 要执行的方法；
# 　　name: 进程名；
# 　　args/kwargs: 要传入方法的参数。
#
# 实例方法：
#
# 　　is_alive()：返回进程是否在运行。
#
# 　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
#
# 　　start()：进程准备就绪，等待CPU调度
#
# 　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
#
# 　　terminate()：不管任务是否完成，立即停止工作进程
#
# 属性：
#
# 　　authkey
#
# 　　daemon：和线程的setDeamon功能一样
#
# 　　exitcode(进程在运行时为None、如果为–N，表示被信号N结束）
#
# 　　name：进程名字。
################################################################################
import time
from  multiprocessing import Process

# def foo(i):
#     time.sleep(1)
#     print (p.is_alive(),i,p.pid)
#     time.sleep(1)
class foo(Process):
    def __init__(self):
        super(foo, self).__init__()
    def run(self):
        time.sleep(1)
        self.alive = self.is_alive()
        print(self.alive)
        time.sleep(1)
if __name__ == '__main__':
    p_list=[]
    for i in range(10):
        p = foo()
        #p.daemon=True
        p_list.append(p)

    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

    print('main process end')