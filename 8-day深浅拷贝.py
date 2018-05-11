#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/17

import copy

'''
深浅拷贝
'''



'''
浅copy只会copy第一层
深copyhuicopy到最后一层
'''

'''
深copy
'''
a = [[1,5],2,3]
b = copy.deepcopy(a)
b[2] = 5
b[0][1] = 2
print(a)
print(b)
'''
[[1, 5], 2, 3]
[[1, 2], 2, 5]
'''


'''
浅copy
'''
a = [[1,5],2,3]
b = a.copy()
b[2] = 5
b[0][1] = 2
print(a)
print(b)
'''
[[1, 2], 2, 3]
[[1, 2], 2, 5]
'''

'''
普通复制
'''
a = [[1,5],2,3]
b = a
b[2] = 5
b[0][1] = 2
print(a)
print(b)
'''
[[1, 2], 2, 5]
[[1, 2], 2, 5]
'''

a = 5
b = a
b = 6
print(b)
print(a)