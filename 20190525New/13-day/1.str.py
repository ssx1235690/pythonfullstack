# -*- coding: utf-8 -*-
# @Time    :  2019/6/20 20:18
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.str.py

## 字符串是不可变对象， 是有序可迭代的对象

song =  "lele yao !!"
song = 'lele yao !!!'
song = """
乐乐 妖 ！！！！！！
"""

##  index 特性

print(song[2])



### 可迭代性

for i in song:
    print(type(i),i)
### join方法 返回str

lis = list(range(5))
print('  DKJDKQQQ  '.join(map(str,lis)))



#### split 方法默认贪婪匹配更多的空格

print(song.split())
print(song.split(' '))

print(song.split('！',2))
print(song.rsplit('！',2)[-1])

print(song.splitlines())  # 默认  \r \n  \r\n

# partition  只切一刀  但是返回元组  而且保留我们的分隔符号
print(song.partition('妖'))

# 全大写
print(song.upper())
#全小写
print(song.lower())

#首字母大写
print(song.capitalize())

# 居中

print(song.center(200))

# 替换

print(song.replace('妖','!---',1))

# stripe  lstripe  rstripe  还可以指定字符集来去除

song = 'wo ai lele yao, very very very much'

print(song.strip(' verymuch'))

# find
print(song.find('very'))

# with open(r'E:\pythonfullstack\20190525New\13-day\1.排序和冒泡法则.py','r',encoding='utf8') as song:
#     for i in song.readlines():
#         print(i)


# print(list(enumerate(song)))


# index 方法找不到会返回一个数值
try:
    print(song.index('verxxy'))
except Exception as  ll:
    print(ll)
