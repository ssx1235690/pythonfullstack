# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 21:45
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.函数执行流程.py

def foo1():
    print('foo1')
def foo2():
    foo3()
    print('foo2')
def foo3():
    foo1()
    print('foo3')

def main():
    foo1()
    foo2()

if __name__ == '__main__':
    main()