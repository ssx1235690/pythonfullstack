# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 23:26
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.习题copy.py


src = 'song1.txt'
dest = 'song2.txt'

xx = open(src,'a+',encoding='utf8')
xx.write('卢卡斯京东方垃圾但是覅爱哦二级覅哦算法ja')
xx.close()

def copy(src,dest):
    with open(src,'r+',encoding='utf8') as x1:
        with open(dest,'w+',encoding='utf8') as x2 :
            x2.write(x1.read())


copy(src,dest)
