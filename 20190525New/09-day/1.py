# -*- coding: utf-8 -*-
# @Time    :  2019/6/4 18:39
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.py

#### 计数位数 脚本
num = input('give me a num ')
num = int(num)
flag = 10
wei = 0
while num > 1 :
    print(num%10)
    num = num // 10
    wei += 1
else:
    print(wei,'位数')