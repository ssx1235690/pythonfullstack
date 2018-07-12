#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 14:03
# @Author  : sxsong
# @Site    : 
# @File    : 22-day并发聊天.py
# @Software: PyCharm


import socket
import select
sk=socket.socket()
sk.bind(("127.0.0.1",8801))
sk.listen(5)
inputs=[sk,]
while True:
    r,w,e=select.select(inputs,[],[],5)
    print(len(r))

    for obj in r:
        if obj==sk:
            conn,add=obj.accept()
            print(conn)
            inputs.append(conn)
        else:
            data_byte=obj.recv(1024)
            print(str(data_byte,'utf8'))
            inp=input('回答%s号客户>>>'%inputs.index(obj))
            obj.sendall(bytes(inp,'utf8'))

    print('>>',r)
