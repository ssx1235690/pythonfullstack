# -*- coding: utf-8 -*-
# @Time    :  2019/9/28
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.正则


import re

# 正则 重点是  分组  断言 去贪婪

# 分组

# 无名组
s='<div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">更多</a><p>dfsl</p></div>'

print(re.search(r'<a.*>(.*)</a>',s).group(1))
# 命名组
s = "ip='230.192.168.78',version='1.0.0'"

print(re.search(r"ip='(?P<ip>\d+\.\d+\.\d+\.\d+).*", s).group('ip'))

# 后向引用
print(re.search(r'(?P<name>go)\s+(?P=name)\s+(?P=name)', 'go go go').group('name'))
print(re.search(r'(go)\s+\1\s+\1', 'go go go').group())




# 断言

# 前向断言
# (?=pattern)
# 后向断言
# (?<=pattern)
# 需要注意的是，如果在匹配的过程中，需要同时用到前向肯定断言和后向肯定断言，那么必须将后向肯定断言写在正则语句的前面，前向肯定断言写在正则语句的后面，表示后向肯定模式之后，前行肯定模式之前。
s1='''char *a="hello world"; char b='c'; /* this is comment */ int c=1; /* t
his is multiline comment */'''

print( re.findall( r'(?<=/\*).+?(?=\*/)' , s1 ,re.M|re.S))

# 前向否定断言、后向否定断言

# 前向否定断言语法：

# (?!pattern)

# 后向否定断言语法：

# (?<!pattern)


# 去贪婪

# *? 重复任意次，但尽可能少重复
# +? 重复1次或更多次，但尽可能少重复
# ?? 重复0次或1次，但尽可能少重复
# {n,m}? 重复n到m次，但尽可能少重复
# {n,}? 重复n次以上，但尽可能少重复



# 正则表达式引擎


re.IGNORECASE