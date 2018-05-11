#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/4/3
import socket
########client端的重要部分 socket.socket connect ,recv, send.sendall
sk = socket.socket()

address = ('127.0.0.1',9876)
sk.connect(address)
data = sk.recv(1024)
print(str(data,'utf8'))
while True:
    data = input('>>>')
    sk.send(bytes(data,'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))
    if str(data,'utf8') == 'quit':
        break
sk.close()