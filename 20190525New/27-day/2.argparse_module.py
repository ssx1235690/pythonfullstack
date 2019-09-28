# -*- coding: utf-8 -*-
# @Time    :  2019/9/28
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : argparse_module

'''
ls -1
ls -la
ls -l -a
ls -l --all
ls -1 -l --all
'''

import argparse
parser = argparse.ArgumentParser(prog='ls',description='List information about the FILEs ',add_help=True)
parser.parse_args()
parser.add_argument('path')
parser.add_argument('-l',action='store_true')
parser.add_argument('-a','--all',action='store_true')

parser.print_help()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

args = parser.parse_args('-l --all /etc'.split())   # 这里要是使用元组进行传参
print(1,args,type(args))