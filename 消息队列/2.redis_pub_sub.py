# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 22:38
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.redis_pub_sub.py


import redis

conn = redis.Redis(host='192.168.157.132')
conn.publish("fm 104.5","hello redis")
conn.sub
