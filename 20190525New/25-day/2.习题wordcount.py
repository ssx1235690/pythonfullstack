# -*- coding: utf-8 -*-
# @Time    :  2019/7/19 9:10
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.习题wordcount.py


d = {}

with open('song1.txt','r+',encoding='utf8') as  context:
    for words in context:
        words = words.split()
        for word in map(str.upper,words):                      ### 使用map函数还可以控制word的大小写问题
            d[word]  =  d.get(word,0) + 1

d = sorted(d.items(),key=lambda d:d[1],reverse=1)

print(d)

