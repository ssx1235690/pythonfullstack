#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/5/7
import socket
import subprocess
import os,sys

sk = socket.socket()
print(sk)
address = ('127.0.0.1',9876)
sk.bind(address)
sk.listen(3)
print('waiting')



conn,addr = sk.accept()

Base_dirname = os.path.dirname(os.path.abspath(__file__))
print(Base_dirname)


while True:
    data = conn.recv(1024)

    cmd,file_name,file_size = str(data,'utf8').split('|')
    path = os.path.join(Base_dirname,'picture',file_name)


    # try:
    #     data =  conn.recv(1024)
    # except Exception:
    #     break
    # if not data: break
    # data = str(data,'gbk')
    # obj = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
    # obj = obj.stdout.read()
    # data = input('>>>')
    # if data == 'quit':
    #     break
    f = open(path,'wb')

    has_recieved = 0
    while has_recieved != file_size:
        data = conn.recv(1024)
        f.write(data)
        has_recieved += len(data)
    f.close()
    print('上传成功')
conn.close()