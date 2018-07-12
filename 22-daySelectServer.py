#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/7/11

import socket,select

sk1 = socket.socket()
sk1.bind(('127.0.0.1',12451))
sk1.listen(2)
sk2 = socket.socket()
sk2.bind(('127.0.0.1',12452))
sk2.listen(2)
while True:
    r,w,e = select.select([sk1,sk2],[],[])

    print("++========================++")
    print(r)


    for i in r:
        conn,addr = i.accept()
        print("+++++===========addr and  conn  的值============++++++++")

        print(addr)
        print(conn)

        print("+++++=======================================++++++++")


        song = input('gei me a password')
        conn.send(song.encode('utf8'))
