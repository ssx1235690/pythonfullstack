#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/4/3

import socket
from PIL import Image
# img=Image.open(r'C:\Users\ronglian\pythonfullstack\picture\socket.jpg')
# img.show()
# socket.socket(family=AF_INET,type=SOCK_STREAM)
# family=AF_INET,表示ipv4 AF_INET6表示ipv6 UNIX表示socket通信
# type SOCK_STREAM 表示tcp连接 SOCK_Dgram表示 udp连接
######server端的scoket 方式 先是创建对象 socket.socket() 在bind ，listen ，accept ，recv，send，sendall
sk = socket.socket()
print(sk)
address = ('127.0.0.1',9876)
sk.bind(address)
sk.listen(3)
print('waiting')
conn,addr = sk.accept()
# print(type(conn))
print(conn)

conn.send(bytes('约啊','utf8'))
while True:
    data =  conn.recv(1024)
    print(str(data, 'utf8'))
    data = input('>>>')
    conn.send(bytes(data,'utf8'))
    if data == 'quit':
        break

conn.close()
