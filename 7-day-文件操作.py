#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/10

'''
python 对文件的操作有三个步骤 1 打开文件创建对象  2 对象调用方法进行操作  3 文件关闭
python3 文件打开的方式就剩下open
r 读模式    read readline readlines
w 写模式    write
a 追加写 指针有坑要注意   write

encoding 方法将文字指定为指定的文件字符
'''

import time
import sys
import  os
files = open('7-day-file','r',encoding='utf-8')
print(files.fileno())
song = files.read()
print(song)
files.close()
files = open('7-day-file','r',encoding='utf-8')
song = files.read(15)  #read 后的数字表示读取的字符数 空格也算在内
print(files.fileno())
print(song)
files.close()
'''
files = open('7-day-file','a',encoding='utf-8')
files.write('\n hello my lele !!!')
time.sleep(50)
files.close()
文件刷新到磁盘的标志使close你要知道只有close 才能搞定这一切 python脚本默认有close的机制但是他是在脚本执行完成之后
append 模式下指针指向最后一个\n之前所以我们要想换行就要在添加的内容前加上一个\n



'''
#time.sleep(3)

a = open('7-day-file','r',encoding='utf-8')



files = open('7-day-file','r',encoding='utf-8').readline() #一行行拿数据
#files = open('7-day-file','r',encoding='utf-8').readlines() #全拿数据，得到列表
print(type(files))#<class 'list'>
print(files)
for i in a:
    print(i.strip())
'''
默认是这种写法，会自动生成迭代器很给力！
'''
a.close()
a = open('7-day-file','r',encoding='utf-8')
a.read(16)
print(a.tell())# tell英文字符是一个字符，但是中文是三个字符这就是python3中的变化
a.close()
#files.flush()  #在默认文件在内存中修改，当所有内容修改完毕，且执行close刷新到磁盘，但flush提供了立即刷新功能
'''
raceback (most recent call last):
  File "C:/Users/Public/pythonfullstack/7-day.py", line 60, in <module>
    files.flush()
AttributeError: 'str' object has no attribute 'flush'
'''


'''进度条就是阐释了flush功能'''
for i in range(30):
    sys.stdout.write("*")
    print('*',end='',flush=True)#print内置很多功能
    sys.stdout.flush()
    time.sleep(0.1)

'''
truncate 截断功能，就是更改文件的写入指针很给力----
当在w方式中调用文件先会被清洗，然后在根据truncate指定的个数跳转
当在啊a方式中打开的时候那么我们就会很给力的真心地
'''



#混合模式
'''
w+  只是支持了读功能，本质上还是清空再写入
r+  如果不读只写他默认从开头写，只要存在读内容他就在最后写
a+  与r+最大的区别是我们不进行读操作它也会在最后  指针默认在最后
'''

'''
files1 = open('7-day-file','r+',encoding='utf-8')
print(files1.readline())
files1.write('song')
print(files1.tell())
files1.close()

       静夜思
        李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡。song
'''

'''
files2 = open('7-day-file','w+',encoding='utf-8')
files2.readline()
files2.write('song')
print(files2.tell())
files2.close()

song
'''


files2 = open('7-day-file','a+',encoding='utf-8')
#files2.readline()
files2.write('song')
print(files2.tell())
files2.close()

#files2.seek() 调整指针位置