# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 23:17
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.base64解码.py


#使用 可变字节类型

import base64

alphbet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'    #源码表

alph = b'jfaoiweronaoinfoiaisfoiaAKJIHIOHIFkhfshAHsJH/+'           #待转换二进制


def base64decode(src:bytes):
    ret = bytearray()    # 最终转换目标
    length = len(src)

    r = 0
    step = 3

    for offset in  range(0,length,step):
        if offset + step <= length:
            tripe = src[offset:offset+3]
        else:
            tripe = src[offset:]
            r = 3 - len(tripe)
            tripe += b'\x00'*r


        b = int.from_bytes(tripe,'big') # 大端模式  网络传输默认为大端模式  window 内部为小端模式
        # f = b.to_bytes(1000,'big')
        # print(f)
        # print(b)
        for i in range(18,-1,-6):
            index = b >> i & 0x3F
            ret.append(alphbet[index])
        for i in range(1,r+1):
            ret[-i] = 0x3D
    return ret


print(base64decode(alph))

########## 使用原生  base64 的方法进行转码验证

zz = base64decode(alph)
ll = base64.decodebytes(zz)
print(ll)
#
# # song = b'abc'
# # c = int.from_bytes(song,'big')
# # print(c >> 18)
# # print(song[18])
#
# song = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# zz = ''
# for i in song:
#     zz += i
# print(zz)
# print(zz.upper())