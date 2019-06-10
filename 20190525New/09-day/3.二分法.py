# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 22:30
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.二分法.py

fen = int(input(' your scores ；'))

if fen > 80:
    if fen > 89:
        print('A')
    else:
        print('B')
elif fen >59:
    if fen > 69:
        print('C')
    else:
        print('D')
else:
    print('E')