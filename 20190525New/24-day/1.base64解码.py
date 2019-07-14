# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 23:17
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.base64解码.py


#使用 可变字节类型

alph = b'jfaoiweronaoinfoiaisfoiaAKJIHIOHIFkhfshAHsJH/+'


def base64decode(src:bytes):
    ret = bytearray()
    length = len(src)

    r = 0
    step = 3
    tripe = bytes()
    for offset in  range(0,length,step):
        if offset + step <= length:
            tripe += src[offset:offset+3]
        else:
            tripe += src[offset:]
            r = 3 - len(tripe)
            tripe += r*b'\x00'


    b = int.from_bytes(tripe,'big')
    print(hex(b))

base64decode(alph)