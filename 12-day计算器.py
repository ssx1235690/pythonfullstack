#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/29
import re,sys
'''
要求：
1\实现加减乘除及拓号优先级解析
2\用户输入
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
运算后得出结果，结果必须与真实的计算器所得出的结果一致
'''
kuohao = re.compile('\([^()]+\)')
strs = input('geime your function')
def check(s):
    if re.findall('[a-z,A-Z]',s):
        print('valid input')
        flag = False
    else:
        flag = True
    return  flag
def format(s):
    s=re.sub(' ','',s)
def jiajian():
    pass
def chengxhu():
    pass
if check(strs):
    format(strs)
    while re.findall('\('):
        kouhao.findall():
        chengxhu()
        jiajian()
    else:
        chengxhu()
        jiajian()
