# -*- coding: utf-8 -*-
# @Time    :  2019/10/20
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.windowmake


import datetime
import random


def test():
    while True:
        yield {
            "song" : datetime.datetime.now(),
            "num" : random.randint(1,10)
        }
s = test()
items = [next(s) for _ in range(3)]
print(items)



# print(sum({
#             "song" : datetime.datetime.now(),
#             "song1" : datetime.datetime.now()
#         }.values()))