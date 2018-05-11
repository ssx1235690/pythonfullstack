#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/1/28
name = "my \tname is {name}, age is {age}."

'''
print(name.capitalize())                #这段话的首字母大写
print(name.count("a"))                  #统计这段字符串中一共有多少个a
print(name.casefold())                  #多语言下的lower
print(name.center(50,"-"))              #一共打印50个字符，把原始字符串放到中间，两边不够的用“-”补上
print(name.encode())                    #把字符串转换成二进制
print(name.endswith("an"))              #判断一个字符串以什么结尾，比如如果以an结尾，就返回True，否则返回False
print(name.startswith('my'))        #判断字符串是否以my开头
print(name.expandtabs(30))              #把字符串中的tab转换成多个空格，这里转换成了30个空格
print(name.expandtabs(tabsize=30))      #把字符串中的tab转换成多个空格，这里转换成了30个空格
print(name.find("name"))               #返回字符串中第一个name的下标，下面示例其中一个切片用法
print(name[name.find("aaron"):])
'''
print(name.format(age=26,name="aaron fan"))   #format的具体用法在day1的interaction交互与字符串格式.py那个脚本中有示例
print(name.format_map({'age':26,'name':'aaron fan'}))   #以字典的形式传送，结果同format
print("123aBc".isalnum())               #判断字符串中是不是同时包含字母和数字，如果同时包含了字母和数字，而且没有包含其它空格和任何特殊字符那么就返回True
print("AaronFan".isalpha())     #判断字符串中是不是只有英文字母，如果只有英文字母而其没有其它数字、空格和任何特殊字符，就返回True
print("123".isdecimal())        #判断是否为十进制
print("123".isdigit())          #判断是否为整数，这个用的比较多，在购物车那个脚本中有使用示例，可以去看一下
print("test123".isidentifier())      #判断是否为一个合法的变量名
print("123".isnumeric())        #判断是否只包含数字
print("    \t      \t".isspace())   #判断是否为空格
print("Aaron Fan".istitle())    #判断首字母是否全部为大写
print(name.isprintable())       #判断这个东西是否可以打印，用到的时候再去详细查下吧
print("AARON FAN".isupper())       #判断是否全部大写
#join的用法
list1 = ["1","2","3","4","5"]
print("+".join(list1))

print(name.ljust(100,"*"))             #打印100个字符串，不够的话右边的全部用指定字符来填补，这里用*
print(name.rjust(100,"*"))              #左边用*填充
print("Aaron FAn".lower())          #把大写变成小写
print("Aaron FAn".upper())          #把小写变成大写
print(name.lstrip())        #去除左边的换行
print(name.rstrip())        #去除右边的换行
print(name.strip())         #去除两边的换行
#print(name.maketrans())
#print(name.translate())
#maketrans和translate加一起可以用来创建一个随机密码，通过自己定义的一个规则，用到时再详细查下吧
print("aaron fan".replace("n","N",1))       #替换字符串中的指定字符，这里的示例是替换其中一个n，使其变成N，值替换1个，也可以替换多个
print("aaron fan".rfind("n"))   #从左网友数，找到最右边的那个值的下标
print("aaron+fan".split("+"))      #把字符串按照指定字符分成一个列表，默认以空格分割成一个列表
print("aaron\nfan".splitlines())    #按照换行符，把字符串分割成一个列表
print("Aaorn Fan".swapcase())       #把大写转小写，小写转成大写
print(name.title())                     #所有单词的首字母都大写
print("123".zfill(100))             #不够100个数字，前面就用0来填充

print("祝各位身体健康", end=' ')    #不换行
print("！")