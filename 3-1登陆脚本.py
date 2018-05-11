#!/usr/bin/python
# -*- coding: utf-8 -*-
print('hello world!')
'''Python 3.0 was released发布 in 2008. The final最终 2.x version 2.7 release came out in mid-2010,
with a statement声明 of extended延长 support支持 for this end-of-life release. The 2.x branch分支 will see no new major重大 releases after that.
3.x is under active development 正在活跃的开发 and has already已经 seen有了 over超过 five years of stable稳定的 releases版本, including包括 version版本 3.3 in 2012,
3.4 in 2014, and 3.5 in 2015. This means意味着 that all recent近期的 standard标准的 library库 improvements升级/改进, for example例子, are only
'''
song = 'xiang'
xiang = song
print(xiang)
song = 'song'
print('what is the value of xiang %s'%(xiang))
print('''

python 的 变量默认是指针类的不会连锁反应
当然后面会有深拷贝的概念慢慢理解就好！！！！

''')
PI = 3.1415926
print('全部大写的变量就认为是常量不对其做改变如PI %f' %(PI))


print('''

python 中也有变量回收的机制他有专门的线程去处理
但是我们也可以使用del 类似shell的unset 来暴力拆除

''')
del xiang


# 用户输入交互
age = int(input('give me your age :'))
total = 88
print('you have ',total - age ,'yearsto live')


"""
a = 0
while a < 3:
	user = input("give me you username: ")
	passw = input("give me you password: ")
	if user == "root" and passw ==  "123456":
		print ("access successfully")
		break
	else:
		a += 1
		print ("you have %d chance to leave" %(3-a))
else:
    print ("hai ta ma shi!!!")
"""
'''
s = 'songshenxiang'
print (s.replace('song','Song'))
print (s.capitalize())
print (s.strip('xiang'))#元素无序贪婪匹配去除
print (s[0])
print (s[0:3])
'''
a = 0
while a < 3:
    user = input('give me your user name: ')
    passwd = input('give me you user pass:')
    if user == 'root' and passwd == '123456':
        print ('acess successful!!')
        break
    else:
        a += 1
        print ('you have %d chances to leave !!!' %(3-a))
        if a == 3:
            flag = input('do you want one more chance /Y for yes:')
            if flag == 'Y':
                a = 0
else:
    print ('bie shi le ni ge laji ')



print('''
python 只要保持缩进一样就可以执行但是大家都按照官方的建议使用四个空格
python 的双引号的意义是一样的，前往不要纠结 他之所以引入单双引号只是为了搞定一些例如
“I‘am song”
''')
