#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 14:04
# @Author  : sxsong
# @Site    : 
# @File    : 22-day并发聊天client.py
# @Software: PyCharm


import socket
# print(__name__)

sk=socket.socket()
sk.connect(('127.0.0.1',8801))

while True:
    inp=input(">>>>")
    sk.sendall(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,'utf8'))