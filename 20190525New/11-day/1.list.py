# -*- coding: utf-8 -*-
# @Time    :  2019/6/11 21:39
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.list.py

#####################内置数据结构

import math
# 数值型
#  int  float  complex  bool
# 序列对象
#  list str truple
# 键值对
#  set  dict


# print(bool(''))


# math 函数明显的声明数字的大小方向
print(math.floor(2.5),math.ceil(-2.5))
print(math.floor(-2.5),math.ceil(2.5))

#  int 函数是取整数并舍弃一切小数位

print(int(2.6),int(-2.6))

### round 函数是  4舍六入  5取离他最近的偶数

print(round(2.5))
print(round(2.6))
print(round(13.5))
print(round(12.5))


##### 计算取整的陷阱


print(7//2,-7//2,-(7//2))
print(1//2,-1//2,-(1//2))


##### 进制转换   返回 str

bin(123)
hex(123)
oct(123)


#### 判断类型


if  type('sdfsf')  == str :
    print('ok')

# if isinstance(123,str):
if isinstance(123,(str,int)):
    print('ok str')