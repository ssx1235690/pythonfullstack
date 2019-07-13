# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:11
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 4.lru_cache.py


from  functools import lru_cache
import time
import sys
sys.setrecursionlimit(100000)

##### 缓存命令将结果直接返回，不会重复执行函数进行压栈

@lru_cache(maxsize=128,typed=False)
def add(x,y,z=2.5):
    time.sleep(z)
    return x+y

print(add(5,6))
print(add(5.0,6))
print(add(5,6.0))
print(add(5,7))
print(add(5,7,z=1))


@lru_cache(maxsize=20)
def fn(x):
    if x == 1 or x ==2 :
         return 1
    else:
        return fn(x-1) + fn(x-2)


print(fn(600))