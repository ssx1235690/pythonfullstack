# -*- coding: utf-8 -*-
# @Time    :  2019/8/19 10:07
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.wordcount.py


import re


Str = '''
Beijing ABT Networks Co., Ltd. will be listed on Shanghai Stock Exchange's sci-tech innovation board, commonly known as SSE STAR Market, the China Securities Regulatory Commission (CSRC) said in a statement over the weekend.

It did not specify the total amount of funds to be raised.

The company and its underwriter will confirm the IPO date and publish its prospectus following discussions with the stock exchange.

The SSE STAR Market, inaugurated on June 13 and designed to focus on companies in the high-tech and strategic emerging sectors, will ease the listing criteria, such as allowing firms that have yet to make a profit to list, but they will adopt higher requirements for information disclosure.
'''
flag = 0
word_dict = {}
def makekeys(strxx):
    for i in range(len(strxx)):

        if flag == 0:
            start = i

        if i == 0 or re.match('\w',strxx[i]):
            continue
        elif  re.match('\W',strxx[i]) and re.match('\w',strxx[i-1]):
            word_dict[strxx[start,i-1]] += 1
        i += 1
    return  word_dict




def wordcount():
    """
    进行词量统计的一个函数
    原理  分词 ---- 组词典 -----sort  ---返回 top5
    :return:
    """
    pass



print(makekeys(Str))
