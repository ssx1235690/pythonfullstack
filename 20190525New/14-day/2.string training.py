# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 11:36
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.string training.py


# 使用数组计数方法，使得计算复杂度降低为  N

num = input('gei me a num:  ')
if num.isdigit():
    pass
else:
    if num.startswith('-'):
        num = num.strip('-')

print('数字长度为 {}'.format(len(num)))
lists = [0] * 10
for i in num:
    lists[int(i)] += 1
else:
    print(lists)



for i in range(-1,-len(num),-1):
    print(num[i])