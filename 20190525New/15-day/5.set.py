# -*- coding: utf-8 -*-
# @Time    :  2019/6/24 9:53
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.set.py

# 树状图是一种数据结构，它是由n（n>=1）个有限结点组成一个具有层次关系的集合。把它叫做“树”是因为它看起来像一棵倒挂的树，
# 也就是说它是根朝上，而叶朝下的。它具有以下的特点：每个结点有零个或多个子结点；没有父结点的结点称为根结点；
# 每一个非根结点有且只有一个父结点；除了根结点外，每个子结点可以分为多个不相交的子树；

# print(hash(tuple(1,2,[1,2])))

import  random


# 集合运算

# set 是一个无序不重复的数列  可以用 set() 或者{} 来表示 但是空集合必须为  set()  集合的值必须可hash

song = set()
song = {1,2,3,4,5,6,6,6,6,6,6,6}
song =  set('12345666666')
print(type(song))
print(song)

# 并集 union

lele = set('12312312332454298472987459827384')
print(lele.union(song))
# print(lele.update(song))  # 就地修改返回 None
print(lele | song)

# 交集

print(song & lele)
print(song.intersection(lele))

# 差集   A－B　B-A　不一样


print(song - lele)
print(song.difference(lele))
print(song.symmetric_difference(lele))
# print(song.difference_update(lele))

# 是否为子集  是否没有交集


print(song.issubset(lele))
print(song < lele)
print(song.issuperset(lele))
print(song > lele)



print(song.isdisjoint(lele))

