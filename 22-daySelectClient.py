#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/7/11

import socket
while 1:
    sk1 = socket.socket()
    sk1.connect(('127.0.0.1',12452))

    song = sk1.recv(1024)
    print(song.decode('utf8'))
    print("++=========+++")
    sk2 = socket.socket()
    sk2.connect(('127.0.0.1',12451))

    song = sk2.recv(1024)
    print(song.decode('utf8'))