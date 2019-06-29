# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 22:10
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.递归原理.py

### 函数本身调用本身就叫递归

import datetime
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