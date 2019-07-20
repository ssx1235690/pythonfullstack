
# -*- coding: utf-8 -*-
# @Time    :  2019/7/19 13:34
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 5.pathlib.py


########### python 3 有专门的path对象  对路径进行操作
from pathlib import Path

p = Path()
p = Path(__file__)
print(p,type(p))

print(p.absolute())

print(p / 'a')  #当前目录下的a吧  这个对象对 / 进行重写

print(p.absolute().parts)   ########目录分割

print(p.absolute().parent.parent)


for i in p.absolute().parents:
    print(i)


print(p.stem)
print(p.name)
print(p.suffix)

print(p.with_name('tomcat').name)
print(p.with_suffix('.xml'))

