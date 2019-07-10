# -*- coding: utf-8 -*-
# @Time    :  2019/7/3 15:44
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.类型注解.py


def add(x:int,y:int):
    """
    :param x:
    :param y:
    :return:
    """
    return x + y

print(help(add))
print(add(1,2))
print(add.__annotations__)
print(add.__annotations__['x'])
print(type(add.__annotations__['x']))

#### 为了不改变python 动态语言的性质，没有对参数的类型作强制判断


# inspect 向内看 检测函数的所有参数

from inspect import  signature
import inspect


def foo(a, *, b:int, **kwargs):
    pass
sig = signature(foo)
print(str(sig))


print(str(sig.parameters['b']))


def a(a, b=0, *c, d, e=1, **f):
    pass

aa = inspect.signature(a)
print("inspect.signature(fn)是:%s" % aa)
print("inspect.signature(fn)的类型：%s" % (type(aa)))
print("\n")

bb = aa.parameters
print("signature.paramerters属性是:%s" % bb)
print("ignature.paramerters属性的类型是%s" % type(bb))
print("\n")


for i,items in enumerate(bb.items()):
    param = items[1]
    print(i,param.default,param.empty,param.kind,param.annotation)



# 使用实例


def check(fn):
    def inner(*args,**kwargs):
        sig = inspect.signature(fn)
        param = list(sig.parameters.values())
        for i,valu in enumerate(args):
            if isinstance(valu, param[i].annotation):
                print('ok')
            else:
                raise TypeError

        return fn(*args,**kwargs)
    return inner


@check
def add(x:int,y:int) -> int:
    return x+y
print(add(22,'dsdfsf'))