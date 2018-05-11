#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/3
'''格式化输出'''
import os
import sys
print(sys.argv)
song = os.popen('dir').read()
print(song.encode('utf8'))
print(song.decode())
name = input('name:')
age = input('age:')
job = input('job:')
salary = input('salary:')
if salary.isdigit():
    print('lower')
    exit(300)
msg = '''
-----info of %s -----
Name: %s
Age: %s
Job: %s
Salary: %s
--------end-----------
'''%(name,name,age,job,salary)
print(msg)


for i in range(1,3):
    name = input('your account:')
    password = input('your password:')
    if name == 'root' and password == '123456':
        print('access successfully!')
        break
    else:
        print('invalid username or password ,please try again!!')
else:
    print('bu yao lian')
# python 的 独特else 别的语言一般不能用ok？


# -------------列表------------
'''
列表的查
列表切片的取值顾头不顾尾
列表切片的时候可以传入三个值第一个值是起始第二个值是结尾（不顾尾）第三个值是步进可以省略省略就是1
步进可以是负值表示从右到左
'''
a = ['xiaoyao','xiaoyu','jinxin','xiaohu','openstack']
print(a[3])
print(a[1: ])
print(a[1:-1])
print(a[1:-1:2])
print(a[-1:1:-2])
'''
xiaohu
['xiaoyu', 'jinxin', 'xiaohu', 'openstack']
['xiaoyu', 'jinxin', 'xiaohu']
['xiaoyu', 'xiaohu']
['openstack', 'jinxin']
'''
print(len(a))  # print(a.__len__()) 表示的内容一样
'''
列表的增加
append 表示追加 insert 插入(位置，要插入的字符串) extend 是列表吞并
'''
a.append('song')
print(a)
a.insert(1,'song')
print(a)
b = [1,2,3]
b.extend(a)
print(b)
'''
['xiaoyao', 'xiaoyu', 'jinxin', 'xiaohu', 'openstack', 'song']
['xiaoyao', 'song', 'xiaoyu', 'jinxin', 'xiaohu', 'openstack', 'song']
'''

'''
列表的修改
类似于变量的重新赋值但是在python中支持变量的多元赋值
'''
a[1:3] = ['limos','limoss']
a[1] = 'liemo'
print(a)

'''
列表的删除
remove 根据值删除
pop 根据index删除，相当于堆栈的操作有返回值
del 删除变量搞定它
'''
a.remove('limoss')
print(a)
print(a.pop(1))
'''
列表计数
count 计数操作
index 是指出它的索引值
'''
print(b.count(2))
print(b.index('xiaoyao'))
print(a[1].find('xiao'))

print(type(b) is list)
'''
列表方向
reverse
'''
print(a)
a.reverse()
print(a)
'''
['xiaoyao', 'jinxin', 'xiaohu', 'openstack', 'song']
['song', 'openstack', 'xiaohu', 'jinxin', 'xiaoyao']
'''
'''
排序
sort
'''
x = [5,8,4,6,3,4,2,31,33,32]
x.sort()
print(x)
'''
[2, 3, 4, 4, 5, 6, 8, 31, 32, 33]
'''


help(list())