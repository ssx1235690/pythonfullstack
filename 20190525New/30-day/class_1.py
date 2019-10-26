# -*- coding: utf-8 -*-
# @Time    :  2019/10/26
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.class

class Person():
    age = 10
    name = 'tim'
    higheit = 175
    def __init__(self,name,age=14):
        self.age = age
        self.name = name
        self.oldname = Person.name
        self.higheit += 100

song = Person('lele')

print(Person.name,song.name)

print(Person.__dict__.items())
Person.name = 'little'

### 定义前后之分

#### 类的变量是所有对象公有的，实例的变量属于自己 ，都可以动态更改,当实例不存在同名变量是  读取类的变量 如 higheit
print(song.__dict__.items())

print(Person.higheit,song.higheit)