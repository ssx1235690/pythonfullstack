# -*- coding: utf-8 -*-
# @Time    :  2019/6/29 7:59
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.insertion sort.py

import random
song = [random.randint(1,30) for x in range(10)]


song = [0] + song
print(song)

for i in range(2,len(song)):
    song[0] = song[i]
    j = i -1
    if song[j] > song[0]:
        while song[j] > song[0]:
            song[j+1] = song[j]
            j -= 1
        song[j+1] = song[0]
print(song)

