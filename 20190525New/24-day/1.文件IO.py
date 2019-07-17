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


song = open('song.txt','r+',encoding='utf8')
print(song.read(2))
print(song.tell())
song.seek(4,0)
print(song.read(1))

############# 文本模式打开的情况下
# seek  有两个参数 a b  a是偏移量   b是位置参数   0开头  1相对于当前  2尾   b=1 时a只能 0
#  seek 移动的是字节 ，而tell 告知的是字符位
# 否则会报错
# Traceback (most recent call last):
#   File "E:/pythonfullstack/20190525New/24-day/1.文件IO.py", line 25, in <module>
#     song.seek(5,1)
# io.UnsupportedOperation: can't do nonzero cur-relative seeks
############### 二进制模式打开
#
#  seek  有两个参数 a b  a是偏移量   b是位置参数   0开头  1相对于当前  2尾
# b = 0  a 只能是整数   其余可正可负






