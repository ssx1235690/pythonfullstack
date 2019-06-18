# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 23:07
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.随机数和元组.py


import  random
print(random.randint(1,6)) # 返回[a,b] 之间的数字
print(random.randrange(1,6)) # 返回 [a,b) 之间的数字  但是可以指定步长

print(random.choice([1,2,4,5,2,4,5,5,23]))  # 选出一个
print(random.sample([1,2,4,5,2,4,5,5,23], 2))  # 选出指定个


print(random.shuffle([1,2,3,4,5]))  # 就地打乱，没有返回值