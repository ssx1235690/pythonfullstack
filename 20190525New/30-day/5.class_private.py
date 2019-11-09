# -*- coding: utf-8 -*-
# @Time    :  2019/10/27
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.class_private


class test():
    __age1 = 123
    def __init__(self):
        self.name = 'abc'
        self.show_age()
    def  show_age(self):
        self.__age = 18
        print(self.__age)
    @property
    def age(self):
        return  self.__age
    @age.setter
    def age(self,a):
        self.__age =  a
print(test.__dict__)
print(test().__dict__)
ll = test()
print(ll.age)
ll.age = 89

###  单下划线 保护变量 python 不提供保护  双下划线是私有变量python 负责保护 如  '_test__age1': 123, ' 即重命名

# 使用property 方法来限制客户输入，控制变量赋值

