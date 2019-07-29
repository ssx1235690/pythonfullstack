# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 23:06
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.argparser.py

import  argparse

parser = argparse.ArgumentParser()

parser.add_argument('path')


# E:\pythonfullstack\20190525New\26-day>python 2.argparser.py ok
# 1 Namespace(path='ok') <class 'argparse.Namespace'>
# ok


args = parser.parse_args()

print(1,args,type(args))

print(args.path)