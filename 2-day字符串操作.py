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

song='   lele is a lovely son, forver lovely !  '
# 1.查找 字符
print(song.find('e'))
print(song.find('e',0,len(song)))

# 2.切片操作
print(song[1:2])
print(song[:2])
print(song[2:])
print(song[-1:-5])

#3 .字符串相加
# 和Java中的字符串一样，不能直接改变字符串的值，更新字符串时候可以用切片技术

song1 = 'lele' + song[12:19]
print(song1)

# 4. 将字符串第一个字符大写
print(song.strip().capitalize())

# 5.将整个字符串小写

song.casefold()

# 6. 字符串居中

print(song.center(25))

# 7.count（sub[,start[,end]]）:sub从start到end出现的次数（默认是整个字符串）

print(song.count('e'))

# 8. endswith（sub）判断是否是以哪个字符串结尾

print(song.endswith(' '))

# 9.isalnum（）:判断s是否是数字或者字母
print(song.isalnum())

# 10. isspace（）：判断是否是空格
print(song.isspace())

# 11. isdigit（）：判断是否都是数字组成

print(song.isdigit())

# 12.isalpha（）：判断是否都是由字母组成的

print(song.isalpha())

# 13.islower（）：判断是否都是由小写字母组成的

print(song.islower())

# 14.istitle（）：判断是否是标题形式字符串（即是连续字符串只有第一个字母大写，其他都是小写，若是有空格，则每个分隔的字符串都满足此）

print(song.istitle())

# 15 isupper（）：判断是否都是由大写字母组成的

print(song.isupper())

# 16. join（sub）

print(song.join('++'))


# 17. lstrip（）：去掉字符串左边所有空格

print(song.lstrip(''))

# 18.rstrip（）：去掉字符串右边的空格

print(song.rstrip())
# 19. replace（old,[,new][,count]）:将字符串中的old子串替换为new，替换count次

print(song.replace('lele','leleyao'))
print(song.replace('leleyao','lele'))

# 20.rfind（sub[,start][,end]）:从右边开始查找字符串中子串从start到end出现的位置并返回下标（注意start和end是从左往右的，返回的也是从左到右的位置。）

song.rfind('lele')


# 21.split（sep）：将字符串用给定的标准分割，并且以列表形式返回分割后的元素组

print(song.split(' '))


# 22.startwith（sub[,start][,end]）:判断从start到end是否以sub开头

print(song.startswith('lele'))

# 23. strip（）：去掉字符串左右两边的空格

print(song.strip())

# 24.swapcase（）：将字符串的大小写反转

print(song.swapcase())

# 25. title（）将字符串标题化（即是连续字符串的第一个字母大写，其他都是小写空格，分隔的字符串都遵循此规则）

print(song.title())

# 26 translate    转换

print(song.maketrans('s','b'))

# print(song.translate())

# 27.upper（）：将整个字符串都大写

print(song.upper())


# 28.zfill（width）：用'0'来填充不够的空格（是从左边开始填充）

print(song.zfill(55))

# 29.lower（）：将整个字符串都小写

song.lower()


# 30. 格式化

print('%d' %(2))

# 31. format()
'{0} love {1}{2}'.format('I','my','home')
'{a} love {b} {c}'.format(a='I',b='my',c='home')