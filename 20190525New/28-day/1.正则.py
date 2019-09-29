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


# 匹配ipv4 地址

ip_str = '''
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:db:d2:ec brd ff:ff:ff:ff:ff:ff
    inet 192.168.137.2/24 brd 192.168.137.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:2f:ce:dc:91 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:2fff:fece:dc91/64 scope link 
       valid_lft forever preferred_lft forever
4: br-e8e12e53a0ef: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ce:97:26:a5 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 scope global br-e8e12e53a0ef
       valid_lft forever preferred_lft forever
    inet6 fe80::42:ceff:fe97:26a5/64 scope link 
       valid_lft forever preferred_lft forever
10: veth69c3c07@if9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-e8e12e53a0ef state UP group default 
    link/ether c6:62:a5:ef:ed:00 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::c462:a5ff:feef:ed00/64 scope link 
       valid_lft forever preferred_lft forever
16: veth1343d63@if15: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-e8e12e53a0ef state UP group default 
    link/ether 1a:a8:31:cb:ff:93 brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::18a8:31ff:fecb:ff93/64 scope link 
       valid_lft forever preferred_lft forever
'''


ll = re.findall(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',ip_str)
print(ll)