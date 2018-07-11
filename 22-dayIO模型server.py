#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 11:38
# @Author  : sxsong
# @Site    : 
# @File    : 22-dayIO模型server.py
# @Software: PyCharm

import socket,time
sk = socket.socket()
sk.setsockopt
sk.bind(('127.0.0.1',5678))
sk.listen(3)


sk.setblocking(False)
while 1:
    try:
        conn,addr = sk.accept()
        while 1 :
            data = conn.recv(1024)
            print(str(data,encoding='utf8'))
            conn.send(data)
            conn.close()
    except Exception as song :
        print(song)
        time.sleep(3)
