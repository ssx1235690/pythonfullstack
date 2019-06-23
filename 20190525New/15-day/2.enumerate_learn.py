# -*- coding: utf-8 -*-
# @Time    :  2019/6/23 21:29
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.enumerate_learn.py

# 使用枚举功能实现 矩阵转置 enumerate 函数
list1 = list(enumerate(range(10)))
print(list1)

list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]


list1 = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [4,6,8]]

### 算法一
list3 = []
count = 0
list2 = enumerate(list1)
for i in list1:
    for j,values in enumerate(i):
        if len(list3) < j + 1:
            list3.append([])
        list3[j].append(values)
        count += 1
else:
    print(list3)





###### 算法二   先生成对应 矩阵模型，再进行脚标互换


tm = [[0 for i in range(len(list1))] for j in range(len(list1[0]))]
print(tm)

for i,row in enumerate(list1):
    for j,row2 in enumerate(row):
        tm[j][i] =  list1[i][j]

print(tm)