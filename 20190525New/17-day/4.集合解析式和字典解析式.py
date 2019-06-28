
# -*- coding: utf-8 -*-
# @Time    :  2019/6/28 22:13
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 4.集合解析式和字典解析式.py


# 语法 { 返回值  for循环}

# song = {[x] for x in range(20)}

# TypeError: unhashable type: 'list'

# print(song)


# 语法 {返回值  for 循环}  返回值为字典


song = {x:x for x in range(5)}
print(type(song))