# -*- coding: utf-8 -*-
# @Time    :  2019/6/24 8:53
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.封装和解构.py



### 封装和解构 的概念    a,b,c = 1,2,3

"""
原理默认是右侧返回元组，左侧在一一对照
对右侧线性结构，进行封包，依次赋予右侧值
其中非线性结构如通常所见的字典变量，也可以进行此类操作
"""

a = 1,2,3
print(a)

b = (1)
print(type(b))


list1 = [1,23]
a,b = list1
print(a,b)


############  个数必须匹配
a,b = '12'
print(a,b)
# a,b = '123'
# print(a,b)
# a,b = '1234'
# print(a,b)


a,b = {'ss':12,'sdfsf':34}
print(a,b)


a,*b = {1,23,445}
print(a,b,sep='----------')




a,*b,c = {1,445}
print(a,b,c,sep='----------')

#   *b 表示尽可能多的 如果变量数多于值 ，那他可以是一个空列表



####################  丢弃变量  python 中使用 _ 表示这个结构的变量可以被舍弃，这是代码规范

a,*_,c = 'sdfsfdasdfafasfadfk'
print(a,c)
# print(_)  # 不要使用这样的自定义变量


a,*a,c = 'sdfsfdasdfafasfadfk'
print(a,c,sep='  much ok  ')