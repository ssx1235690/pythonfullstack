#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/7/11

import socket

sk = socket.socket()
sk.connect('127.0.0.1',12452)
while 1:
