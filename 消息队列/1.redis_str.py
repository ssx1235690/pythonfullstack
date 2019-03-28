# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 22:23
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.redis_str.py
import redis

conn = redis.Redis(host='192.168.157.132',db=10)
conn.set("song",1123)
song=conn.get("song")
print(song)