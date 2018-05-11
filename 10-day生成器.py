#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/16



#####################生成器############################
#####列表生成式######
a = [ x for x in range(10) ]
print(a)

a = [ x*x for x in range(10) ]
print(a)

def foo(x):
    return x * x
a = [ foo(x) for x in range(10) ]
print(a)
#####python的赋值方式#####
t = [1,2]
a,b=t
print(a,b)

#######生成器就是吧中括号变成小括号######
a = ( x*x for x in range(10) )
print(type(a))#<class 'generator'>
#生成器的概念是有一种方法代替了大量数值，节省了内存，你给出一个index返回给你一个值
print(a.__next__())
print(next(a))
'''
上述两种方法是等价的
0
1
'''
#生成器的调用一般是使用for 循环
for i in a:
    print(i)
#根据python的内存回收机制但没有变量指向这个内存单元的时候他就释放，生成器恰恰是一个个吐非常省内存

#####另外一种生成生成器的方法是这样yield
print("另外一种生成生成器的方法是这样yield")
def foo():
    print('ok')
    yield 1
    print('ok2')
    yield 2
g=foo()
k=foo()
next(k)
print(next(k))
'''
ok  直接next的话生成器对象会走print 然后yield一个值但是没有打印
ok2  再加上print 回取回返回值
2
'''



# #斐波那契数列函数
# def fqnb(max):
#     n,before,after = 0,0,1
#     while n < max:
#         print(after,end='   ####    ')
#         before,after = after,before+after
#         '''
#         上述等价于
#         tmp=before
#         before=after
#         after+=tmp
#        '''
#         n += 1
# fqnb(500)

#上述函数改写成生成器
def fqnb2(max):
    n,before,after = 0,0,1
    while n < max:
        yield before
        before,after = after,before+after
        n += 1
song= fqnb2(80)
print(song)

##send的功能

def sendtest():
    print('ok1')
    count = yield 1
    print(count)
    yield 2
jj = sendtest()
next(jj)
ret=jj.send('nidaye')
###普通的函数只能一溜烟的执行，生成器是一步步的能进行控制，可以产生并发
###alex吃包子伪并发
def consumer(name):
    print('%s准备吃包子'%(name))
    while True:
        baozi = yield
        print('%sa包子被%s吃了'%(baozi,name))
def producer(name):
    c = consumer('A')
    c1 = consumer('B')
    next(c)
    next(c1)
    print('准备吃包子')
    for i in range(10):
        print('做了2个包子')
        c.send(i)
        c1.send(i)
        i+=1
producer('song')

#要看明白生成器的每次迭代，就像是完成函数未完成的步骤一样