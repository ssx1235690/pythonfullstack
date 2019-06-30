# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 22:10
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.递归原理.py

### 函数本身调用本身就叫递归

import datetime
import sys
sys.setrecursionlimit(100000)


lstart = datetime.datetime.now()

############# 递归 代码精炼 但是不断的 压栈 效率很低   且递归有最大深度限制

def fbnc(n):
    return 1 if n < 2 else fbnc(n-1) + fbnc(n-2)


# print(fbnc(33))

lstop = datetime.datetime.now()
print((lstop - lstart).total_seconds())



##########  只要循环逻辑正确  循环的效率高
def fbnc(n,pre=1,cur=1):
    if n < 2 :
        return 1
    else:
        for i in range(2,n+1):
            pre,cur = cur,pre+cur
    return cur
print(fbnc(135))




######################  阶乘问题     Christian Kramp

def song(n):
    return 1 if n ==0 or n ==1 else  n*song(n-1)

print(song(6))


####################  数字反转

def song(n,list=[]):
    n,p = divmod(n,10)
    list.append(p)
    if n >0:
        song(n)
    return list


print(song(12312238887887342))


################ 猴子吃桃问题

def peach(day):
    if  day > 9:
        return 1
    return (peach(day+1) +1)*2
print(peach(day=1))



