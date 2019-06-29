# -*- coding: utf-8 -*-
# @Time    :  2019/6/28 22:46
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.可变参数.py


def song(*x,**y):
    print(x)
    print(y)

song(1,2,3,4,5,b=8,c=8)
# song(b=8,c=8,1,2,3,4,5)
# SyntaxError: positional argument follows keyword argument

# 参数的位置 总结为   普通参数 > 缺省参数 > 可变位置参数 *x  > keyword-only 参数 >可变关键字参数  **y


#
# def song(**sss,x):
#     pass
#
#     def song(**sss,x):
#                    ^
# SyntaxError: invalid syntax


#####################################
####################################  参数解构

def song(x,y):
    print(x,y)
song(*(1,2))
song(*[1,2])

song(*range(2))


#### 结构字典时   key必须为 字符串  变量名必须合法

def song(**kwargs):
    print(kwargs)

song(**{'sdf':123,'sdfasdf':234})


#### 以下类型注意对应

# def song(x,y):
#     print(x,y)
# 
# song(**{'sdf':123,'sdfasdf':234})
#
# TypeError: song() got an unexpected keyword argument 'sdf'



# 解构符号  在print 函数中的使用  ，虽然format 功能强大，但是这样的写法我们也要能理解

print(*[1,234,53453])