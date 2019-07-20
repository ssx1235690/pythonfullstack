# -*- coding: utf-8 -*-
# @Time    :  2019/7/19 10:50
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.StringIO和BytesIO.py


from io import StringIO,BytesIO

sio = StringIO()   #类文件对象
sio.write('song lele  yao ')
print(1,sio.read())
print(sio.seek(0))
print(2,sio.read())
sio.close()


with StringIO() as leleyao:
    leleyao.read()


with  BytesIO() as leleyao:
    leleyao.write(b'sdfjkajklsjdflkjaklsjdkf')

# 两个类都是在系统中开辟的一块 buffer 空间。当close函数执行时会被释放

###  下列三种句柄  不要收到关闭
from  sys import stdout,stderr

f = stdout
f = stderr
f.write('sfsdfsdf')