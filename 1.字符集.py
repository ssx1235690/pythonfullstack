#!/usr/bin/python
# -*- coding: utf-8 -*-
msg='''
如果用二进制数字来表示26个英文字母
001 a
010 b
011 c
100 d
真正的（ASCii）表格也类似这样他是先由字母和特殊字符转换成数字然后数字再转换成二进制
一个字母占一个字节 就是8个二进制单位。
gbk 占两个字节
utf-8 占三个字节
计算机的容量单位
1 Byte =  8 bit
1kB = 1024 Byte
1M = 1024 KB
1G = ...
1T = ...
 python 是89年诞生的一条小蛇，现在逐渐的变化成一条大蛇大蟒蛇。
'''
print(msg)

# python3中默认使用unicode编码模式，比起其他更胜一筹，太给力了。
# 编码就是将字符串转换成字节码，涉及到字符串的内部表示。
# 解码就是将字节码转换为字符串，将比特位显示成字符。
# str->bytes:encode编码
# bytes->str:decode解码
# bytes.decode(encoding="utf-8", errors="strict")
# str.encode(encoding="utf-8", errors="strict")