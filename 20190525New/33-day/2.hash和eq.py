# -*- coding: utf-8 -*-
# @Time    :  2020/3/15
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.hash和eq

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self,a,b):
        self.c = a+b

    def f(self):
        return 'hello world'

num1 = MyClass(2,3)
num2 = MyClass(2,3)

print([num1,num2])
print((num1,num2))
print({num1,num2})


'''
[<__main__.MyClass object at 0x00823470>, <__main__.MyClass object at 0x00823490>]
(<__main__.MyClass object at 0x00823470>, <__main__.MyClass object at 0x00823490>)
{<__main__.MyClass object at 0x00823490>, <__main__.MyClass object at 0x00823470>}
'''

# 构造hash函数 当哈希函数一致时 比较 eq函数 如果结果为真 在集合中会去重


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self,a=25,b=26):
        self.b =b
        self.c = a+b

    def f(self):
        return 'hello world'
    def __hash__(self):
        return 123
    def __eq__(self, other):
        return self.b == other.b


num1 = MyClass(2,3)
num2 = MyClass(2,3)

print([num1,num2])
print((num1,num2))
print({num1,num2})

