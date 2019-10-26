# -*- coding: utf-8 -*-
# @Time    :  2019/10/27
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.class_private


class test():
    __age1 = 123
    def __init__(self):
        self.name = 'abc'
    def  show_age(self):
        self.__age = 18
        print(self.__age)
print(test.__dict__)
print(test().__dict__)


###  单下划线 保护变量 python 不提供保护  双下划线是私有变量python 负责保护 如  '_test__age1': 123, ' 即重命名