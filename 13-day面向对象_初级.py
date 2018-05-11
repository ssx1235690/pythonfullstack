#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/3/1
#函数式
def foo(name,age,gender,action):
    print(name,age,gender,action)
foo('song','12','男','like')
foo('song','12','男','sleep')
foo('song','12','男','work')

#对象式
class bar:
    def foo(self,name,age,gender,action):
        print(self,name,age,gender,action)
        return name
obj = bar()
print(obj)
name = obj.foo('song','12','男','like')
obj.foo('song','12','男','sleep')
obj.foo('song','12','男','work')
print(name)
# 类的封装，类在创建的时候不止会有一个自己的self变量，还有一个正经的构造函数当生成对象的时候会自动生成。
class bar:
    def __init__(self):
        self.name = 'song'
        self.age = 12
        self.gender = 'nan'
    def foo(self,content):
        print(self.age,self.name,self.gender,content)
obj = bar()
obj.foo('shang shan')

#类的继承关系，即子类。子类可以选择性的继承父类，原理就是覆盖，在子类中重新定义父类中函数

class bar_song(bar):
    def foo(self):
        print(self)
obj = bar_song()
obj.foo()

# 子类也可以执行父类中的方法在定义的函数中
# 1.使用super方法  super(子类名，self).父类中的方法（）
# 2.使用 父类名.父类中方法（self,）
class bar_song(bar):
    def foo(self):
        super(bar_song, self).foo('song')
        bar.foo(self,'song')
        print(self)
obj = bar_song()
obj.foo()
#子类在继承多了父类的时候存在顺序问题(只有python 和 C++ 才支持这种写法，其他语言像C 如果同时继承多个父类，
# 它在加载同名函数的时候会报错因为他没有这种处理机制)
# 1.左侧优先
# 2.当有共同的父类的时候从左侧开始查找覆盖，当左侧没有时再从右侧查找覆盖,最后才会找到父类.
class A():
    def a(self):
        print('a')
class B():
    def a(self):
        print('b')
class C(A,B):
    pass
obj = B()
obj.a()

class base():
    def a(self):
        print('base a')
class F1(base):
    def a(self):
        print('F1 a')
class F2(base):
    def a(self):
        print('F2,a')
class F3(F1,F2):
    pass
obj = F3()
obj.a()
#
#####一种复杂的情况，调用的函数中出现self.函数名时。由于self 代表对象本身，求索函数的过程又从头开始。
class base():
    def process(self):
        print('base.process')
class F1(base):
    def sever(self):
        print('F1.sever')
        self.process()
    def process(self):
        print('F1.process')
class F2():
    def process(self):
        print('F2.process')
class son(F2,F1):
    pass
obj = son()
obj.sever()



#######多态的问题#########
