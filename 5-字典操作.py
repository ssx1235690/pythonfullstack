#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/3
'''
没有考虑到二维以上的数据关系xxx
'''
'''
goods = [('iphone6s',5500),('mac',12000),('python book',80),('coffee',32),('bicycle',1500)]
salary = input('请输入要充值数目')
if salary.isdigit():
    for i in enumerate(goods,1):
        print(i)
    for i,j in enumerate(goods, 1):
        print(i,'>>>>',j)
'''
'''
enumerate 增加索引 还可以指定索引开始数值
1 >>>> ('iphone6s', 5500)
2 >>>> ('mac', 12000)
3 >>>> ('python book', 80)
4 >>>> ('coffee', 32)
5 >>>> ('bicycle', 1500)
'''
'''
    for i in range(1,len(goods)+1):
        print('%d %-5s %-15s'%(i,goods[i-1][0],goods[i-1][1]))

1 iphone6s 5500           
2 mac   12000          
3 python book 80             
4 coffee 32             
5 bicycle 1500
'''
'''
先堆出大的逻辑架构复杂的语句走pass
然后我们好好的学习这些东西
重复的事不做第二遍
'''


'''
字典是无序的，键值唯一的我了个去他大姨妈
'''
'''
字典的增加
'''
#字典的创建过程是这样的可以使用dict函数传入列表或元组也可以直接指定添加
dict1=dict((['song','name'],))
print(dict1)
dict1['age']=27
print(dict1)
#设置字典值的默认值，如果该键值存在就返回该键值。
dict1.setdefault('age',34)
red=dict1.setdefault('age',34)
print(dict1)
print(red)
'''
字典的查
'''
#取出字典中所有的键
print(list(dict1.keys()))# 取出所有的键
print(list(dict1.values()))#取出所有的值
print(list(dict1.items()))#取出所有的信息
'''
['song', 'age']
['name', 27]
[('song', 'name'), ('age', 27)]
True
'''
print('song' in dict1)

'''
字典的更改
'''
dict2 = dict1
dict3 = {'1':'123','2':'235'}
dict2.update(dict3)
print(dict2)
# {'song': 'name', 'age': 27, '1': '123', '2': '235'}
'''
列表的删除
'''
del dict2['1']
print(dict2)
dict2.clear()
print(dict2)
print(dict3.pop('1'))
print(dict3)
dict3 = {'1':'123','2':'235'}
print(dict3.popitem()) # 随机删除一组键值对垃圾，并返回值
print(dict3)
'''
{'song': 'name', 'age': 27, '1': '123', '2': '235'}
{'song': 'name', 'age': 27, '2': '235'}
{}
123
{'2': '235'}
('2', '235')
{'1': '123'}
'''

'''
其他操作
'''
dict4 = dict.fromkeys(['name','age','host'],['song','26','10.0.0.201'])
print(dict4)
'''
{'name': ['song', '26', '10.0.0.201'], 'age': ['song', '26', '10.0.0.201'], 'host': ['song', '26', '10.0.0.201']}
'''
dict4['name'][1] = 27
print(dict4)
'''
{'name': ['song', 27, '10.0.0.201'], 'age': ['song', 27, '10.0.0.201'], 'host': ['song', 27, '10.0.0.201']}
'''
dict5 = dict4.copy()
dict5['name'][1] = 22
print(dict4)


import json
print(json.dumps({'#xiaoyao':dict4},sort_keys=True,indent=4))

'''
字符串操作
单双引号没有区别，只是为了引号嵌套方便
'''
a = '123'
b = 'abc'
c = a+ b

print(c)
c = '------'.join([a,b])

print(c)
'''
123abc
123------abc
'''
c = a.join(b)
'''
a123b123c
'''
print(c)
#string的内置方法
st = 'hello lele! {name}{age}'
print(st[4:9:2])
print(st.capitalize()) #Hello lele!
print(st.isdigit())  #判断是不是数字
print(st.isalnum())
print(st.isalpha())

print(st.find('el',3,)) #找到指定内容首次出现的位置并返回的索引位置，还可以指定起始位置
#print(st.index('到',4,8))
'''
index 和 find 的区别是当查找不存在的情况下 index会报错
 File "C:/Users/Public/pythonfullstack/5-shopcar讲解.py", line 152, in <module>
            "song",
    print(st.index('到',4,8))
            22,
            "10.0.0.201"
ValueError: substring not found
'''
print(st.expandtabs(3))#生成制表符没用

print(st.center(50,'#'))#居中
print(st.endswith('el')) #判断结尾
print(st.startswith('he')) #判断开头
print(st.count('l',1,))  #查找个数
print(st.format(name='song',age=15))#格式化输出，识别字符串中默认的{}中定义的变量

print('345adb'.isidentifier())

print(' '.isspace())
print(st.isupper())
print(st.islower())
print(st.istitle()) #是否单词首字母大写
print(st.swapcase()) #大小写反转

print(st.strip('h')) #取出字符串首尾的指定字符
print(st.lstrip('h'))
print(st.rstrip('!'))


print(st.replace('hello','song'))

'''
空格分割join联合
'''
print(st.split(' '))
song = st.split(' ')
print(' '.join(song))
