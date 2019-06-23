# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 9:00
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.string format.py


### printf format C 风格

song = """
wo ai lele yao !!!!!
"""

print('wo ai %s !!!!!' %('lele yao',))
# print('wo ai %s !!!!!' %['lele yao'])

print('%3.2f%%  ox%x,OX%02X' %(89.4563,16,17))


#### print  format 函数

print('{{}}'.format())  ######### {{}}  打印花括号


print('{0:>10x}'.format(97))
print('{0:>10b}'.format(97))
