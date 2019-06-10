# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 23:25
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.99乘法表.py

for i in range(1,10):
    for j in range(1,10):
        if i >= j :
            # s = str(i)+'*'+str(j)+'='+str(i*j)
            # print(s,end=' ',sep='\t')
            print('{}*{}={}'.format(i,j,i*j),end='\t',sep=' ')
    print()


print('$$$$$$$$$$$$$$$$$$$$$############################')


for i in range(1,10):
    for j in range(1,10):
        if i <= j :
            # s = str(i)+'*'+str(j)+'='+str(i*j)
            # print(s,end=' ',sep='\t')
            print('{}*{}={}'.format(i,j,i*j),end='\t',sep=' ')
        else:
            print('{} {} {}'.format(' ', ' ', '  '), end='\t', sep=' ')
    print()