# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 14:42
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1. 字符集和编码.py


# 字符串是字符组成的有序数列，字符可以用编码来理解
# bytes 是字节组成的有序数列，且不可改变
# bytearray  是字节组成的有序可变的序列

# str  encode  bytes
#
# bytes  bytearray  decode  str

song = '乐乐妖'

print(song.encode(encoding='utf8'))
print('a'.encode(encoding='utf8'))

print(b'a'.decode())


# bytes 函数的用法
print('bytes 函数的用法' )


bytes(5) #填充指定位数的utf8 空串


# bytes(可迭代对象)  返回一个 bytes序列
print(bytes([0,1,2,3,4,5]))

# find 方法

print('     我爱北京天安门'.encode('utf8').find('我'.encode('utf8')))


# hex()  和   fromhex方法

zz ='我爱北京天安门 ！！！！ oh yeah!!!!'.encode('utf8').hex()
print(zz)

print(bytes.fromhex(zz).decode())


###  bytesarray 方法可变的 bytes   追加 清楚  remove  pop  改变值只能为 数字类型

zz = bytearray(b'abc')
zz1 = b'abc'

zz.replace(b'a',b'bb')
zz1.replace(b'a',b'bb')
zz[2]  = 101
print(zz)
print(type(zz))