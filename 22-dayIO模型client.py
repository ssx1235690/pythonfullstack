#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 11:38
# @Author  : sxsong
# @Site    : 
# @File    : 22-dayIO模型client.py
# @Software: PyCharm

import socket
sk = socket.socket()
sk.connect(('127.0.0.1',5678))
print(sk)
while 1:
    # song = input('please  input  something')
    # song = bytes(song,encoding='utf8')
    song = bytes('hello lele',encoding='utf8')
    sk.send(song)
    song = sk.recv(1024)
    print(song)