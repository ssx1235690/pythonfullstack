#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/1/28
s = 'song shen xiang lele de baba'
print(s.capitalize())
print(s.title())
print(s.find('xi'))
print(s.replace('lele','leleyao'))
print(s.split(' '))
#########字符串中自带一些查找功能但是他只支持完全匹配。要使用模糊匹配只能使用我们的re模块#######3
#http://www.cnblogs.com/yuanchenqi/articles/5732581.html

import re

ret = re.findall('a..in', 'helloalvin')
print(ret)  # ['alvin']
'''
就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言，（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。

字符匹配（普通字符，元字符）：

1 普通字符：大多数字符和字母都会和自身匹配
              >>> re.findall('alvin','yuanaleSxalexwupeiqi')
                      ['alvin'] 

2 元字符：
.  任意一个字符
^  以什么开头
$  以什么结尾
*  任意个数的任意字符
+  一个以上的任意字符
?  0或1个任意字符
{ } 指定个数的任字符数
[ ] 期中字符的任意一个
|    或者关系
( )  一组
\   转义字符 
#######################################################
反斜杠后边跟元字符去除特殊功能,比如\.
反斜杠后边跟普通字符实现特殊功能,比如\d

\d  匹配任何十进制数；它相当于类 [0-9]。
\D 匹配任何非数字字符；它相当于类 [^0-9]。   中括号加^表取反
\s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
\S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
\w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
\b  匹配一个特殊字符边界，比如空格 ，&，＃等
########################################################
'''
# 前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret=re.findall('abc*?','abcccccc')
print(ret)#['ab']
ret=re.findall('\w',"i am lele's father")
print(ret)
ret=re.findall('I\b','I am LIST')
print(ret)#[]
ret=re.findall(r'I\b','I am LIST')
print(ret)#['I']


##################反斜杠用法########################联想思考我们在shell中使用单引号隔离shell解释器的第一步解释就等于我们加r
print(' -----------------------------eg1:')

#ret=re.findall('c\l','abc\le')
print(ret)#[]
#ret=re.findall('c\\l','abc\le')
print(ret)#[]
ret=re.findall('c\\\\l','abc\le')
print(ret)#['c\\l']
ret=re.findall(r'c\\l','abc\le')
print(ret)#['c\\l']
# -----------------------------eg2:
# 之所以选择\b是因为\b在ASCII表中是有意义的
m = re.findall('\bblow', 'blow')
print(m)
# m = re.search('\bblow', 'blow').group()
# print(m)
'''
Traceback (most recent call last):
  File "C:/Users/ronglian/pythonfullstack/11-day模块re.py", line 78, in <module>
    m = re.search('\bblow', 'blow').group()
AttributeError: 'NoneType' object has no attribute 'group'
'''
m = re.findall(r'\bblow', 'blow')
print(m)
m = re.search(r'\bblow', 'blow').group()
print(m)

##############group#############
ret=re.search('(?P<id>\d{2})/(?P<name>\w{3})','23/com')
print(ret.group())#23/com
print(ret.group('id'))#23
print(ret.group('name'))#23

###################正则表达式的常用方法############################33
# 1
re.findall('a', 'alvin yuan')  # 返回所有满足匹配条件的结果,放在列表里
# 2
re.search('a', 'alvin yuan').group()  # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3
re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配

# 4
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

# 5
ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
print(ret)  # alvinabcyuan6
ret = re.subn('\d', 'abc', 'alvin5yuan6')
print(ret)  # ('alvinabcyuanabc', 2)

# 6
obj = re.compile('\d{3}') #生成对象，直接用对象进行一系列调用。
ret = obj.search('abc123eeee')
print(ret.group())  # 123

#7迭代器
ret = re.finditer('[a,bc]','abcaaabcbcbbc')
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())
ret = re.finditer('a|bc','abcaaabcbcbbc')
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())