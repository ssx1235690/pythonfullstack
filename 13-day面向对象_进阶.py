#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/3/8

# 类的三大成员
# 一、字段
# 字段包括：普通字段和静态字段，他们在定义和使用中有所区别，而最本质的区别是内存中保存的位置不同，
# 普通字段属于对象
# 静态字段属于类
# 对象可以找到类，反之类无法找到对象。
class province:
    #静态
    country = '中国'
    def __init__(self):
         #普通
        self.name = '邢台'
# xintai = province('邢台')
xintai = province()
print(xintai.name)
print(province.country)

#
# 二、方法
# 方法包括：普通方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同。
# 普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
# 类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
# 静态方法：由类调用；无默认参数；

class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        # print self.name
        print ('普通方法')

    @classmethod
    # @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print ('类方法')

    @staticmethod
    # @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print ('静态方法')


# 调用普通方法
f = Foo('王大锤')
f.ord_func()
# Foo.ord_func(f)

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()


# 三、属性　　
#
# 如果你已经了解Python类中的方法，那么属性就非常简单了，因为Python中的属性其实是普通方法的变种。
#
# 对于属性，有以下三个知识点：
#
# 属性的基本使用
# 属性的两种定义方式
#不伦不类的定义和引用我们的，定义是方法的定义方式，引用是普通变量的引用方式

# ############### 定义 ###############
class Foo:

    def func(self):
        pass

    # 定义属性
    @property
    # @property
    def prop(self):
        pass
    @prop.setter
    def prop(self,var):
        print(var)
    @prop.deleter
    def prop(self):
        print('del')
# ############### 调用 ###############
foo_obj = Foo()

foo_obj.func()
foo_obj.prop   #调用属性

foo_obj.prop = 123
del foo_obj.prop

#################属性的另一种定义和调用方式###################
class foo():
    def f1(self):
        print('f1')
    def f2(self,var):
        print('f2',var)
    def f3(self):
        print('f3')
    per = property(fget=f1,fset=f2,fdel=f3)
obj = foo()
obj.per
# obj.per('song')
# import subprocess
# subprocess.call('notepad')