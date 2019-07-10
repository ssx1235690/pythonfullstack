# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 23:19
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.带参数的修饰器.py


### 柯里化  f(x+y) = f(x)(y)

import datetime
import time
import  random
from multiprocessing import  Process
from functools import  wraps

def add(x):
    def xxx(y):
        return x+y
    return xxx
print(add(1)(2))


def logger(fn):
    def wapper(*args,**kwargs):
        lstart = datetime.datetime.now()
        print('arg is {}, kwargs is {}'.format(args,kwargs))
        ret = fn(*args,**kwargs)
        lstop = datetime.datetime.now()
        print('function {} tooks {}s'.format(fn.__name__,(lstop - lstart).total_seconds()))
        wapper.__name__ = fn.__name__
        return ret
    return wapper
@logger
def add(x,y):
    """sdfjlslfjajdfjalsfjja1111"""
    return x+y

# print(add(11,y=66),add.__name__,add.__doc__)



lsum = []

def test(fn):
    @wraps(fn)
    def inner(n):
        # time.sleep(random.randint(10,50))
        print('ok')
        fn(n)
    return inner
@test
def feibo2(n):
    for i in range(0,n):
        if i == 0 or i == 1:
            lsum.append(1)
        else:
            lsum.append(lsum[i-2]+lsum[i-1])
    # print(lsum)
    return lsum
feibo2(10)

if __name__ == '__main__':
    processes = list()
    for i in range(10):
        p1 = Process(target=feibo2, args=(30000,))
        p1.start()
        processes.append(p1)
    for p in processes:
        p.join()
