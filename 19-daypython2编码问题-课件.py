#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/6/13
from PIL import Image

##################### python2 的数据类型###########################
#
# 一共有两种   str   和    unicode
#
# str和unicode都是basestring的子类。严格意义上说，str其实是字节串，它是unicode经过编码后的字节组成的序列。对UTF-8编码的str，
# '松'使用len()函数时，结果是3，因为utf8编码的'苑' == '\xe8\x8b\x91'。
#
# 而unicode是一个字符串，str是unicode这个字符串经过编码（utf8,gbk等）后的字节组成的序列。如上面utf8编码的字符串'汉'。
#
# unicode才是真正意义上的字符串，对字节串str使用正确的字符编码进行解码后获得，并且len(u'苑') == 1。
#
# 在python 2 里，str＝bytes。
#
# python2 编码的最大特点是Python 2 将会自动的将bytes数据解码成 unicode 字符串
#
# 所以在2里我们可以将字节与字符串拼接


print '逍遥lele'                            # 字符串
print repr('逍遥lele')               # \xe9\x80\x8d\xe9\x81\xa5'
print type('逍遥lele')
print (u"hello"+"lele")
'''
如果当头部没有指定    -*- coding: utf-8 -*-  或者 coding:utf8  会出现下列错误
SyntaxError: Non-ASCII character '\xe7' in file C:/Users/ronglian/pythonfullstack/19-day��������-�μ�.py on line 7, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

'''
print u'逍遥lele'                            # unicode
print repr('逍遥lele')               # \xe9\x80\x8d\xe9\x81\xa5'
print type(u'逍遥lele')
print (u"hello"+"lele")

################print(u'逍遥lele'+'翔翔')
'''
Traceback (most recent call last):
  File "C:/Users/ronglian/pythonfullstack/19-day��������-�μ�.py", line 39, in <module>
    print(u'逍遥lele'+'翔翔')
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)

'''
# img=Image.open(r'C:\Users\ronglian\pythonfullstack\picture\19-day图1.png')
# img.show()


u = u'宋'
print repr(u)  # u'\u82d1'
# print str(u)   #UnicodeEncodeError

s = u.encode('utf8')
print type(s)
print repr(s)  # '\xe8\x8b\x91'
print str(s)  # 宋
u2 = s.decode('utf8')
print repr(u2)  # u'\u82d1'