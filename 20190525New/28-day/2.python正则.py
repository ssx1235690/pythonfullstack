# -*- coding: utf-8 -*-
# @Time    :  2019/9/29
# @Author  :  user01
# @Email   : ......998@qq.com
# @File    : 2.python正则


import re

# match  vs  search


s = 'abcdef'
s1 = 'abcdefg'

print(re.match(r'a',s))   # 只匹配开头
print(re.match(r'c',s))
print(re.fullmatch(r'c',s))
print(re.fullmatch(r'abcdef',s))
print(re.fullmatch(r'abcdef',s1))   # 需要完全匹配
print(re.search(r'a',s))
print(re.search(r'c',s))    #包含就行




#  re.split


# re.split(r'(\W+)', '...words, words...')
# ['', '...', 'words', ', ', 'words', '...', '']


#  re.sub(pattern, repl, string, count=0, flags=0)
ll = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
     r'static PyObject*\npy_\1(void)\n{',
     'def myfunc():')

print(ll)


#  re.findall   re.finditer  finditer(pattern, string, flags=0)


ll  = re.findall(r'^|\w+', 'two words')
print(ll)
ll  = re.finditer(r'^|\w+', 'two words')

for m in ll:
    print(m.group(0))


