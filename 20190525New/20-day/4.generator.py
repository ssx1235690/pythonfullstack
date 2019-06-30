# -*- coding: utf-8 -*-
# @Time    :  2019/6/30 13:53
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.generator.py


### 生成器 可以用生成器 表达式 或者 yield 语句实现

def gene(n):
    for i in range(n):
        yield i
ll = gene(10)

print(type(ll))
for i in ll:
    print('**',sep='  ',end=' ')
print('')
for i in ll:
    print('*/*',sep='   ',end=' ')



##############  区别 与 return ， yield 可以重复出现 且不影响


def gene():
    while True:
        print('line 1')
        yield 1
        print('line 2')
        yield 2
        print('line 3')
        yield 3
ll = gene()

for i in range(9):
    next(ll)