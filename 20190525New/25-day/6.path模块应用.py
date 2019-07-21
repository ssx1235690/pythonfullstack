
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 21:07
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 6.path模块应用.py



from pathlib import Path


print(Path().joinpath(*['a','b','c/d']))



p = Path()
print(p.cwd())
print(p.home())  # 返回用户 家目录

print(p.absolute() / 'abc')



print(p.is_dir())
print(p.is_file())

print(p.is_symlink())

# 当文件 是软连接的时候， 有一个 resovle 方法能返回真实指向的文件

