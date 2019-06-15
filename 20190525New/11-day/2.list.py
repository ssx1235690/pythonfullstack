# -*- coding: utf-8 -*-
# @Time    :  2019/6/15 16:05
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.list.py

# a = [1,2,3,4,5]
# print(id(a[1]))
# print(id(a[2]))
# print(id(a[3]))
# print(id(a[4]))

a = [1,2,3,4,5,6,1100]

# index 操作  复杂度  N
a.index(3)

# len  操作 复杂度  1  内部计数器实现


len(a)
#  append 操作 每次只能执行一次

a.append(1111)


# insert  操作 复杂度  N

a.insert(2222,5)


print(a)

# 扩展  将可迭代对象加入其中

a.extend(range(33))


