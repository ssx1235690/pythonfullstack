
#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/5/12

import threading,time,sys

class Account:
    def __init__(self,money,name,r):
        self.blance = money
        self.name = name

    def withdraw(self,num):
        se
        self.blance -= num
    def repay(self,num):
        self.blance += num

song = Account(99999,'songshenxiang')
print(song.blance)

def caozuo(_from,to,count):
    # r = threading.Lock()
    # r.acquire()
    _from.withdraw(count)
    to.repay(count)
    # r.release()
a1 = Account(2000,'song')
a2 = Account(1000,'xiang')

caozuo(a1,a2,500)
print(a1.blance)
print(a2.blance)
