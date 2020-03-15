# -*- coding: utf-8 -*-
# @Time    :  2019/12/1
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.magic_function

def area(width, height):
    return width * height


class A:
    '''
    sdfhajkksdfjasdfasdf
    '''
    pass
print(A.__name__)  #A 是表示符   __name__ 才是真正的变量值 字符串

print(A.__module__)
print(A().__module__)

# A的类型
print(A.__class__)

# A的基类
print(A.__bases__)

# A 的注释
print(A.__doc__)

# 类的继承顺序
print(A.__mro__)

# 字典

print(A.__dict__)


# 收集当前模块的所有值
print(dir())

print(dir(A))
print(dir(area))


# 魔术方法

# 创建 和 销毁

# init  del



