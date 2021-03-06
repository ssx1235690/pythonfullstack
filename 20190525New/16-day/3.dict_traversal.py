# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 23:04
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 3.dict_traversal.py

# 在遍历时无论是增加还是减少，只要改变了我们 字典的大小就会报错
song = {1:'2323',2:'232123','232':'sdfasdf',66:True}
print(song)


for i in song:
    # song.pop(i)
    print(i)
# RuntimeError: dictionary changed size during iteratio

# song.pop(1)
# # song.popitem(True)
# print(song)

list1 = []
for i in song:
    if i == 2:
        list1.append(i)
for i in list1:
    song.pop(i)
print(song)



#### 缺省字典


import  random
from collections import defaultdict

d = {}
d= defaultdict(list)
for i in 'abcdef':
    for j in range(random.randint(1,5)):
        # if not d.get(i):
        #     d[i] = []

        d[i].append(j)
print(type(d))
print(d)



##### 有序字典


from collections import OrderedDict

ll = OrderedDict(a=1,b=2)
print(ll)




sorted({'a': [0, 1], 'b': [0, 1, 2, 3], 'c': [0, 1], 'd': [0, 1, 2, 3], 'e': [0, 1], 'f': [0, 1, 2, 3, 4]}.items(),key=lambda x:x[1])