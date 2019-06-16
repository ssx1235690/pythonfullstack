# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:55
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.list.py


a = [[1,2,3]]
b = a*5
print(b)
b[1][2]  = 5
print(b)

a = ['abc']
b = a*5
print(b)
b[0]  = 5
print(b)

# 二级嵌套的list 存放的是子列表的 内存地址  修改子列表内容， 会出现联动错觉


# remove 从左到右 删除列表内容  复杂度回变化

b.remove('abc')

print(b)

#  pop  指定索引后 删除索引对应数值   不指定索引那么就从 尾部 弹出一个

b.pop(3)
print(b)
b.pop()
print(b)

# clear 清空列表 ， 频繁释放 内存空间受影响

# b.clear()

# reverse 反转

b.reverse()


# sort 方法 就地修改  key传递对value 的处理函数  可以是 类型转换的  str  int  etc..

print(b.sort(key=str))