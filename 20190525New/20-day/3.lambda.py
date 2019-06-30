# -*- coding: utf-8 -*-
# @Time    :  2019/6/30 12:41
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.lambda.py

#### python 使用lambda 关键字来构建我们的 匿名函数表达式


### lambda表达式用 : 隔离开 参数列表和表达式  不需要 return 语句来返回数值


print((lambda x:x**2)(11))

ll =lambda x:x**2
print(ll(23))