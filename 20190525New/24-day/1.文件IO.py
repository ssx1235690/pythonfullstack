# -*- coding: utf-8 -*-
# @Time    :  2019/7/15 14:46
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.文件IO.py



### open 函数


# song = open('song.txt','a')
# song.write('lele yao')
#
# print(song)
# song.close()


song = open('song.txt','rb')
ll = song.read(1)
ll = song.read(1)
print(ll)
song.close()