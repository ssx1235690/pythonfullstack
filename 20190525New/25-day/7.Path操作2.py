
# -*- coding: utf-8 -*-
# @Time    :  2019/7/21 7:49
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 7.Path操作2.py


from pathlib import Path

### 调用文件方法进行 文件操作

p = Path('/a/b/c/e')
print(p.is_dir())

p = Path('a')

p.rmdir()
p.mkdir(755)


