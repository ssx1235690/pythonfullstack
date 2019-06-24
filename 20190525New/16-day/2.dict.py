# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 22:08
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.dict.py


song = dict(a=1,b=3,c=123)
print(song)
song = 1 if 1 else 3

song = dict(([1,'asd'],[2,'sdfds']))
print(song)

song = dict.fromkeys(range(5),[1111])  # 浅拷贝
print(song,id(song[0]),id(song[1]))
# print(song[5])  KeyError

# get方法不会抛出异常
print(song.get(5,10000))
song.setdefault(5,100000)

song.update(((5,100),))
# song.update((5,100))
print(song)


# pop  返回一个单值

song.pop(5)
print(song)


# popitem  返回一个封装

print(song.popitem())