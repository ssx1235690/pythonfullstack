# -*- coding: utf-8 -*-
# @Time    :  2019/7/2 18:45
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.functool.py

import functools
import datetime

def logger(fn):
    @functools.wraps(fn)   ##### 第二步
    def zzq(*args,**kwargs):
        """ this is a doc of zzq"""
        lstart = datetime.datetime.now()
        print('arg is {}, kwargs is {}'.format(args,kwargs))
        ret = fn(*args,**kwargs)
        lstop = datetime.datetime.now()
        # functools.update_wrapper(zzq, fn)                     ### 第一步
        print('function {} tooks {}s'.format(fn.__name__,(lstop - lstart).total_seconds()))
        return ret
    return zzq
@logger
def add(x,y):
    """this is a doc of add"""
    return x+y
print(add(11,66),add.__name__,add.__doc__)

