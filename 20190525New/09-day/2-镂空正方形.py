# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 22:16
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2-镂空正方形.py

lele = input('give me a num :  ')

long = int(lele)

for i in range(long):
    if i == 0 or i ==  long -1:
        print('*\t'*(long-1)+'*')
    else:
        print('*'+'\t'*(long-1)+'*')

