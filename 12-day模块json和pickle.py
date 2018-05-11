#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/2/6


# 我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。



import json,pickle
# song = open('7-day-file','a')
# song.write('{liuliu}')
# song.close()
# 对文件写只能写入字符串，对文件的读也只能读出字符串，如果我们要对字典进行处理那么我们的那么我们一般可以这么操作。
song = '{"song":1,"shen":2}'
# song["song"] TypeError: string indices must be integers
# 1使用eval
song = eval(song)
print(type(song))
# 2使用 dict方法
# >>>dict()                        # 创建空字典
# 2 {}
# 3 >>> dict(a='a', b='b', t='t')     # 传入关键字
# 4 {'a': 'a', 'b': 'b', 't': 't'}
# 5 >>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
# 6 {'three': 3, 'two': 2, 'one': 1}
# 7 >>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
# 8 {'three': 3, 'two': 2, 'one': 1}
# 9 >>>
song=json.dumps(song,indent=4)
print(song,type(song))
print(help(json.dump))
#######################
# ----------------------------序列化
# import json
#
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# print(type(dic))  # <class 'dict'>
#
# j = json.dumps(dic)
# print(type(j))  # <class 'str'>
#
# f = open('序列化对象', 'w')
# f.write(j)  # -------------------等价于json.dump(dic,f)
# f.close()
# # -----------------------------反序列化<br>
# import json
#
# f = open('序列化对象')
# data = json.loads(f.read())  # 等价于data=json.load(f)
###################################pickle##########################
# import pickle
#
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
#
# print(type(dic))  # <class 'dict'>
#
# j = pickle.dumps(dic)
# print(type(j))  # <class 'bytes'>
#
# f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
# f.write(j)  # -------------------等价于pickle.dump(dic,f)
#
# f.close()
# # -------------------------反序列化
# import pickle
#
# f = open('序列化对象_pickle', 'rb')
#
# data = pickle.loads(f.read())  # 等价于data=pickle.load(f)
#
# print(data['age'])
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
# json.dump(要序列化的对象，文件句柄)
# dump和load是一对，dump和load直接把转化结果存入了文件，