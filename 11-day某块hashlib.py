#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/24

import hashlib

m=hashlib.md5()
print(m)
m.update('song'.encode('utf8'))
print(m)
print(m.hexdigest())
m.update('shenxiang'.encode('utf8'))
print(m.hexdigest())