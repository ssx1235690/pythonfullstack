#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/21

msg='''
一组实现某种特定功能的语句进行封装的产物
是这段重复的内容具有 高扩展等性能
'''
def song():
    print('ok')
song()
print(song)
'''
<function song at 0x0000020E5D923E18>
'''
msg='''
形参和实参
'''
print(msg)

def a(x,y):
    return x + y
b = a(5,6)
print(b)
def a(x,y):
   print(x + y)
b = a(5,6)
print(b)
'''
11
None   不适用return的时候结果无法复制给变量
'''
def print_info(name,age,sex='male'):
    print('name is %s,age is %d gender is %s'%(name,age,sex))
#必须参数，必须按位传递
print_info('song',25)
#关键字参数传递时指定变量位
print_info(age=25,name='song')
#默认参数sex会一直打印默认值，重新复制会给予覆盖

#不定长参数
def sum(*args):
    sumory = 0
    for i in args :
        sumory += i
    print(sumory)
    return sumory

sum(5,6,5,8,9)

def print_info(*args,**kwargs):
    print(args,kwargs)
print_info('song',25,565,sex='male',lendd='none')
'''
一个星号保存元组看清楚了不是集合，两个星号保存字典.注意格式问题不能两种格式混写
print_info('song',25,565,sex='male',lendd='none'，55，66)
'''
'''
传入方式还可以使用下列方式
'''
print_info(*[2,3,4,4],**{'name':'liumang'})




def print_info1(name='spark',*args,**kwargs):
    print(args,kwargs)
print_info1('song',25,565,sex='male',lendd='none')
'''
(25, 565) {'sex': 'male', 'lendd': 'none'}
当时用*arg或者**kwargs  的时候我们可以吧默认值写在前面但是它会占位
'''



'''
retrun
1.是的函数的结果能赋值给变量，return还会直接结束函数！！！！return的结果是一个对象 数字字典等等
2.当retrun的值为多个时，合并为一个元组
3.没有返回值是默认为none
'''
def kkk():
    print('ok')
    return  10,'ssdfa',['sdf',55,'sdfadsf']
a=kkk()
print(a)
'''
(10, 'ssdfa', ['sdf', 55, 'sdfadsf'])
'''



'''
能对变量进行重新的定域操作的只有我们的 函数 模块 类
函数的作用域
LEGB
L local
Enclosing 继承父类
global 全部的
built in  关键字级别内置的变量
'''

x = int(3.6)
def e_print():
    e_num = 2
    def l_print():
        l_num = 1
        e_num = l_num
        print(l_num)
        print(e_num)
    l_print()
e_print()
'''
变量解读顺序测试，解读顺序依次是 LEGB一旦找到就不往上层找
1
1
'''
'''
高阶函数和递归函数和内置函数
'''
def a(n):
    return n
def gaojie(a,b,func):
    return func(a) + func(b)
print(gaojie(3,6,a))


def digui(n):
    if n == 1:
        return 1
    return  n * digui(n-1)
print(digui(18))


song = int(8.9)
print(song)

'''
两个最重要的关键字global和nonlocal
global 是修改全局变量的
nonlocal 是用来修改我们的enclose变量的
'''
song = 'song123'
def okboy():
    global song
    song = 12345
    print(song)
okboy()
print(song)
'''
12345
12345
'''

song = 123
print(song)
def okboy2(k):
    k=1234
    print(k)
    def inner():
        nonlocal k
        k = 12345
    inner()
    print(k)
okboy2(song)
'''
123
1234
12345

'''