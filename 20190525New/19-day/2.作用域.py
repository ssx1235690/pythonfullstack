# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 19:46
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.作用域.py
# 作用域：是访问变量时查找变量名的范围
# * python3的四个作用域： LEGB
#
# 作用域	英文解释	英文简写
# 局部作用域（函数内）	Local(function)	L
# 外部嵌套函数作用域	Enclosing function locals	E
# 函数定义所在模块作用域	Global(module)	G
# python内置模块的作用域	Bui	B
# * 变量名查找规则：
# 在访问变量时，先查找本地变量，然后是包裹此函数外部的函数内的变量，之后是全局变量
# 最后是內建作用域内的变量
# 即： L –> E —> G —> B
# ** 在默认情况下，变量名赋值会在当前作用域内创建变量和修改变

def outer():
    o = 65
    def inner():
        print('{}'.format(o))
        print(type(o))
    o += 1
    inner()
outer()

def outer():
    o = 65
    def inner():
        o = 97
        print('{}'.format(o))
        print(type(o))
    o += 1
    inner()
outer()


#### 全局变量和本地变量
x = 1
# def outer():
#     x += 1
#     print(x)
# UnboundLocalError: local variable 'x' referenced before assignmen
# outer()


### global 可以解决上述问题。但是不建议这么去用，很不好。

def outer():
    # x = 0
    global x
    x += 1
    print(x)
outer()


##### 与之相对应  nolocal 可以让内嵌函数使用  E 非全局变量

o =60

def outer():
    o = 65
    def inner():
        nonlocal o
        o += 1
        print('{}'.format(o))
        print(type(o))
    o += 1
    inner()
    print(o)
outer()
