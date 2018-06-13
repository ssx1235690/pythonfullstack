#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 13:59
# @Author  : sxsong
# @Site    : 
# @File    : 19-daypython3编码问题.py
# @Software: PyCharm

from PIL import Image
''' 

python3 renamed the unicode type to str ,the old str type has been replaced by bytes.
python3中将byte和str的名称进行了调换，并将Python2的自动转换转成了手动，防止了编码错乱问题。

跟 Python 2 类似，Python 3 也有两种类型，一个是 Unicode,一个是 byte 码。但是他们有不同的命名。

现在你从普通文本转换成 “str” 类型后存储的是一个 unicode, “bytes” 类型存储的是 byte 串。你也可以通过一个 b 前缀来制造 byte 串。

Python 3最重要的新特性大概要算是对文本和二进制数据作了更为清晰的区分。文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。
Python 3不会以任意隐式的方式混用str和bytes，正是这使得两者的区分特别清晰。你不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然），
也不能将字符串传入参数为字节包的函数（反之亦然）。这是件好事。

'''

img=Image.open(r'C:\Users\ronglian\pythonfullstack\picture\19-day图2.png')
img.show()
'''
Python 3 中对 Unicode 支持的最大变化就是将会没有对 byte 字节串的自动解码。
如果你想要用一个 byte 字节串和一个 unicode 相链接的话，你将会得到一个错误，不管你包含的内容是什么。

所有这些在 Python 2 中都将会有隐式的处理，而在 Python 3 中你将会得到一个错误。

'''
#print('alvin'+u'yuan')#字节串和unicode连接 py2:alvinyuan
# print(b'alvin'+'yuan')#字节串和unicode连接 py3:报错 can't concat bytes to str

'''
Traceback (most recent call last):
  File "C:/Users/ronglian/pythonfullstack/19-daypython3编码问题.py", line 35, in <module>
    print(b'alvin'+'yuan')#字节串和unicode连接 py3:报错 can't concat bytes to str
TypeError: can't concat str to bytes

'''

import json

s='逍遥乐乐'
print(json.dumps(s))   #"\u82d1\u660a"
b1=s.encode('utf8')

print(b1,type(b1))     #b'\xe8\x8b\x91\xe6\x98\x8a' <class 'bytes'>

# print(b1.decode('utf8'))#
print(b1.decode('gbk'))# 閫嶉仴涔愪箰

b2=s.encode('gbk')
print(b2,type(b2))  #'\xd4\xb7\xea\xbb' <class 'bytes'>
print(b2.decode('gbk')) #