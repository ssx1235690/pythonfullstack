#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/5/7
import socket
import subprocess
import os,sys


sk = socket.socket()

address = ('127.0.0.1',9876)
sk.connect(address)

Base_dirname = os.path.dirname(os.path.abspath(__file__))
while True:
    data = input('>>>')  # put 11.png
    cmd,path = data.split(' ')
    path = os.path.join(Base_dirname,path)
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size

    file_info = 'post|%s|%s'%(file_name,file_size)

    sk.sendall(bytes(file_info,'utf8'))

    # with open(path,'rb') as f
    f = open(path,'rb')

    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print('上传完毕')

sk.close()