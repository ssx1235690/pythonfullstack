#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/17

'''
集合和列表字典最大的区别是他的元素不可重复,字典只是键不能重复。同时set 是无序的，还不能像字典一样通过键索引，set只能通过for
循环去遍历和利用迭代来搞基
字典的键一定是可hash的就是不可变的可以是正数，字符串，可以是元组，但不可以是列表
'''

a = {'si':'msdf','sjdfklajs':'sdfasf0','si':'sdfafds','bi':'sdfafds'}
print(a)
#{'si': 'sdfafds', 'sjdfklajs': 'sdfasf0', 'bi': 'sdfafds'}
a = set(a)
# {'sjdfklajs', 'si', 'bi'}
print(a)
song = set(a)
'''
print(a[1])

Traceback (most recent call last):
  File "C:/Users/Public/pythonfullstack/8-day2-set.py", line 16, in <module>
    print(a[1])
KeyError: 1
'''

a = set('song sdfa sdfsd')
print(a)
'''
a = set([{'song':'好玩'},'liumang','sdfasdf'])
    a = set([{'song':'好玩'},'liumang','sdfasdf'])
TypeError: unhashable type: 'dict'

'''

msg='''
set 的内置方法
'''
print(msg)

a = frozenset(['song','shen','xiang'])

a = set(['song','shen','xiang'])
print(a)

a.add('song')
print(a)
a.update('song')
print(a)
'''
{'shen', 'song', 'xiang'}
{'shen', 'song', 'xiang'}
{'shen', 'g', 's', 'o', 'song', 'n', 'xiang'}
update 就是 把添加的元素打散
add 是吧元素作为整体添加
'''
a.remove('o')
a.pop()#随机删除
print(a)
a.clear()
print(a)
del a

msg='''
集合的逻辑（关系测试）
集合的交集子集合集的概念
'''
print(msg)


print(set('songshen')==set('songhe'))
print(set('songshen')>set('ddsonghe'))

a = set('12345')
b = set('456789')
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
print(a.symmetric_difference(b))

'''
set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)等数学运算. 
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。
'''