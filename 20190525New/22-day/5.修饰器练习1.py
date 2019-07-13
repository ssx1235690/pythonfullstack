# -*- coding: utf-8 -*-
# @Time    :  2019/7/13 9:44
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.修饰器练习1.py


###################命令缓存器1

cmds = {}

def register(cmd):
    def _register(fn):
        cmds[cmd]=fn
        return fn
    return _register

def start():
    while True:
        cmd = input("a cmd should be gave or a quit :")
        if cmd  == 'quit' :
            break
        cmds.get(cmd,defafunc)()
def defafunc():
    print('uknown   !!!!!')
@register('ls')
def ls():
    print('command ls')
@register('py')
def py():
    print('command python')
@register('test')
def test():
    print('this is a test print ')



# start()


########### 命令缓存器2

import inspect
import  functools

from collections import OrderedDict
local_cache = {}

def cache(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):

        def make_key(fn):
            # 拿到签名
            sig = inspect.signature(fn)
            params = sig.parameters
            keys = list(params.keys())
            values = params.values()
            # 初始化字典
            params_dict =  OrderedDict()
            # 提取位置参数拼凑字典
            for i,val in enumerate(args):
                k = keys[i]
                params_dict[k] = val
            # params_dict.update(kwargs)  #######  直接update 没有经过排序不好
            # 提取关键字参数拼凑字典
            for k,v in sorted(kwargs.items()):
                params_dict[k] = v
            # 提取缺省参数拼凑字典
            for k,param in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = param.defult

            return tuple(params_dict.items())
        key = make_key(fn)
        if key not in local_cache.keys():
                local_cache[key] = fn(*args,**kwargs)
        print(local_cache)
        return local_cache[key]
    return wrapper

import datetime
import time
def logger(fn):
    @functools.wraps(fn)
    def inner(*args,**kwargs):
        start =  datetime.datetime.now()
        ret = fn(*args,**kwargs)
        end = ((datetime.datetime.now() - start).microseconds)
        print(end,fn.__name__)
        return ret
    return inner




@logger
@cache
def func1(x,y,z):
    time.sleep(2)
    return x+y+z


print(func1(1,2,3))
print(func1(1,2,z=3))
print(func1(1,z=3,y=2))
print(func1(1,3,z=3))
