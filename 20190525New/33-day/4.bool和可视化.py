# -*- coding: utf-8 -*-
# @Time    :  2020/3/17
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.bool和可视化

import json
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self,a,b):
        self.c = a+b

    def f(self):
        return 'hello world'
    def __bool__(self):
        # return False
        return True


print(dir(MyClass))

if MyClass(1,2):
    print('bool  is  ok')



'''
可视化
'''


list1 = [1,2,3,4,5,]
print(*list1)


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self):
        self.c = 1

    def f(self):
        return 'hello world'
    def  __repr__(self):
        return 'repr output '
    def __str__(self):
        return 'songshenxiang'
    def __bytes__(self):
        return json.dumps([123,123]).encode()

print(MyClass())
print([MyClass()])
print([str(MyClass())])
print(bytes(MyClass()))
