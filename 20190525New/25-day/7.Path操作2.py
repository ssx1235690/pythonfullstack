
# -*- coding: utf-8 -*-
# @Time    :  2019/7/21 7:49
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 7.Path操作2.py


from pathlib import Path

### 调用文件方法进行 文件操作

# p = Path('/a/b/c/e')
# print(p.is_dir())
#
# p = Path('a/b/c/d')
#
# p.rmdir()
# p.mkdir(755,parents=True)
#
p = Path('a/b/c/d/1.txt')
p.touch(644)


print(p.parent)
#### 目录递归

p = Path('a')
ll = p.iterdir()   # 自遍历一级
print(ll)
for i in ll:
    print(i)

##### 通配符查找   glob  rglob
p = Path('a/b')

print(p.glob('*txt'))
print(p.glob('**/*txt'))
for i in p.glob('**/*txt'):
    print(i)

for i in p.rglob('*txt'):
    print(i)


ll = list(p.rglob('*txt'))
print(ll)

######  匹配算法  match
p = Path('a/b/c/d/1.txt')
print(p.match('*txt'))

####### 查看状态  stat == lstat  只有当文件为软连接是不同
print(p.stat())
print(p.lstat())