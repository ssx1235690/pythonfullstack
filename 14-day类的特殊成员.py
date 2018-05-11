#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/3/13

########################################## 一、成员修饰符 #################################################
# 共有成员
# 私有成员, __字段名
# - 无法直接访问，只能间接访问

from PIL import Image

class Foo:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.__age = age


obj = Foo('song',12)
obj.name
# obj.age
# obj.__age
# AttributeError: 'Foo' object has no attribute '__age'

#####普通字段的私有化#######
class song:
    def __init__(self):
        self.xiang = 'lele'
        self.__song = 'xiaoyao'
    def pp(self):
        print(self.__song)
# print(song.__song)
# AttributeError: type object 'song' has no attribute '__song'
lele = song()
lele.pp()
######静态字段的私有化########
class song:
    __song = 'yaoyao'
    def show(self):
        return song.__song
lele = song()
print(lele.show())
#######私有的变量只能通过对象间接的访问########

######私有化方法，属性都可以私有化，但是我们一般不会直接私有化属性############
#######私有化可以通过一些验证机制使我们的变量，不会被明码窃取###########


########################################二、特殊成员####################################################
# __init__
# 类()
# 自动执行
# __del__
# __call__
# 对象()
# 类()()
# 自动执行
# __int__
# int(对象)
# __str__
# str()
#
# __add__
# __dict__  # 讲对象中封装的所有内容通过字典的形式返回
# __getitem__  # 切片（slice类型）或者索引
# __setitem__
# __delitem__
#
# __iter__


# 如果类中有 __iter__ 方法，对象=》可迭代对象
# 对象.__iter__() 的返回值： 迭代器
# for 循环，迭代器，next
# for 循环，可迭代对象，对象.__iter__()，迭代器，next
# 1、执行li对象的类F类中的 __iter__方法，并获取其返回值
# 2、循环上一步中返回的对象

class song:
    def __init__(self):
        print('init')
    def __call__(self, *args, **kwargs):
        print('call')
# 调用方式
lele = song()
lele()


###### 解释 为什么可以使用   str  或者 int方法进行类型转换

class song:
    def __init__(self):
        print('init')
    def __int__(self):
        return 111
    def __str__(self):
        return 'xiaoayo'
lele = song()
lele = str(lele)
print(lele)

lele = song()
print(lele)  #使用print 默认就会执行 str函数

################################三、metaclass, 类的祖宗###################################################3
# a.Python中一切事物都是对象
# b.
# class Foo:
#     pass
# obj = Foo()
# # obj是对象，Foo类
# # Foo类也是一个对象，type的对象
# c.
# 类都是type类的对象
# type(..)
# “对象”都是以类的对象
# 类()

class song(type):
    def __init__(self,*arg,**kwargs):
        print(123)
class lele(object,metaclass=song):
    def fun(self):
        print('my lele')
leleyao = lele()


img=Image.open(r'C:\Users\ronglian\pythonfullstack\picture\chaojilei.jpg')
img.show()



####################################### 四、异常处理#################################################
#
# raise Exception('数据库处理错误')
#
# while song != '':
#     try:
#         song = input('geime a num')
#         if song == 123:
#             print('hello')
#         raise SongError('SongError')     #主动弹出错误
#     except IndexError as index:    # 所有的except会顺序执行类似case语句。想要精确捕捉请把 Exception 放到最后方
#         print('index')
#     except Exception as e:   #Exception 是所有的异常的一个父类。
#          print(e.value)
#     else:
#         print('else')  #出错了 会执行 except 语句 ，无错则执行 else
#     finally:       #不管怎样都会执行
#         print('else')
# assert song == ''  # 断言 条件不满足的话，程序就会瞬间死掉。
######################################### 五、反射################################################
#  通过字符串来操作 对象中的成员
class song():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)
lele  = song('song',26)
k1 = 'name'
print(getattr(lele,k1))
print(hasattr(lele,k1))
setattr(lele,'gender','male')
print(lele.gender)
delattr(lele,k1)

####使用实例， 进行输入函数跳转
# s2.py
# def k1():
#     print('k1')
# def k2():
#     print('k2')
#
# s1.py
# import s2
# choice = input('choice')
# getattr(s2,choice)
# ####代替了大量的if else 判断 很可怕。


####################################### 六、单例模式################################################
####数据库连接池的概念，真心好有意思
#####   @classmethod  表示为直接用类来调用函数不用实例化，因为其中的形参为cls 而不是 self

class song:
    __v = None
    @classmethod
    def get_instance(cls):
        __v = song()
        return __v
obj1 = song.get_instance()
obj2 = song.get_instance()
obj3 = song.get_instance()
print(obj1,obj2,obj3)
