# -*- coding: utf-8 -*-
# @Time    :  2019/11/9
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.practice_class

import random

class RandomInt:
    def __init__(self,count=10,start=1,end=100):
        self.count = count
        self.start = start
        self.end
    def geneRand(self):
        return [random.randint(1,100) for _ in range(self.count)]

# 工具类集合

class RandomInt2:
    @classmethod
    def geneRand(cls):
        return [random.randint(1, 100) for _ in range(self.count)]


class RandomInt3:
    """
    改进方式一  使得count 可以改变
    """
    def __init__(self,count=10,start=1,end=100):
        self.count = count
        self.start = start
        self.end
    def geneRand(self,count=0):
        count = self.count if count <=0 else count
        return [random.randint(1,100) for _ in range(count)]


'''
属性方法当 属性名称和setter 内容一致是 会出现死循环 切记
'''

class RandomInt4:
    def __init__(self,start=1,end=100):
        self.start = start
        self.end = end
    @property
    def count(self):
        return [random.randint(1,100) for _ in range(self._count)]
    @count.setter
    def count(self,n):
        self._count = n
song  =  RandomInt4()

song.count=100
print(song.count)