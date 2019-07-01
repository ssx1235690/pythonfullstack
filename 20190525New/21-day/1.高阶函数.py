# -*- coding: utf-8 -*-
# @Time    :  2019/6/30 14:29
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.高阶函数.py

# 高阶函数的概念: 1 接受一个或3多个函数输入  2输出一个函数  满足下列两条之一


def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


f1 = counter(10)
f2 = counter(10)

print(f1==f2)
print(f1 is f2)
print(f1() is f2())

print(f1())
print(f1())
print(f1())
print(f1())
print(f2())


#### 三大高阶函数  sorted  filter  map
def sort_self(iter,reverse=True,key=lambda x,y: x<y):
    ret = []
    for x in iter:
        for i,y in enumerate(ret):
            if  key(x,y) != reverse:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort_self([8,7,6,5,3,4,1,2],reverse=False))


ll = filter(lambda x:x>5,[8,7,6,5,3,4,1,2])
for i in ll:
    print(i)



ll = map(lambda x:x//2+2,[8,7,6,5,3,4,1,2])

for i in ll:
    print(i)