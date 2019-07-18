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
# song.seek(4,0)
print(song.read(1))
song.close()

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
# tell 返回字节数

song = open('song.txt','rb',buffering=1)
print(song.read(3).decode())
print(song.tell())
# song.seek(6,0)
# print(song.read(3).decode())
song.close()


########### 缓冲区   buffering     flush 函数


# 缓冲分三种：
# 全缓冲 : open函数的buffering设置大于1的整数n,n为缓冲区大小，linux默认为page的大小4096 满了n 个字节才会写入磁盘 。
#
# f=open(“demo.txt”,’w’,buffering=1)
# 1
# 行缓冲 : open 函数的buffering设置为1, 碰到换行就会将缓冲区的写入磁盘。
#
# f=open(“demo.txt”,’w’,buffering=1)
# 1
# 无缓冲 : open 函数的buffering设置为0 有输入就写入磁盘。
#
# f=open(“demo.txt”,’w,’,buffering=0)


################## 文件编码


# unicode 万国码   -----> utf-8
song  = '拉萨可见度分厘卡机'
song = song.encode(encoding='utf-8')
print(song)
print(song.decode(encoding='utf8'))

song = open('song.txt','w+',encoding='gbk')
############# 换行
song.write('a\r,slkdjfkl\r\n,slkjdjhfkljasdlf\n')

################### 文件描述符

print(song.fileno())
song.close()



################ 文件上下文关系


song = open('song.txt','r+')
print(song.seekable())
print(song.writable())
print(song.readable())
song.close()

# try:
#     pass
#
# except ValueError as e:
#     pass
#
# except Exception as e:
#     pass
#
# else:
#     pass
#
# finally:
#     pass

#
# 操作文件出错 导致文件 无法close
# 可以使用 try  finaly 方式解决
#     但是python 提供一个更好的方式   with 语句