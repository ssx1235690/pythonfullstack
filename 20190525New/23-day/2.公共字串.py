# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 17:14
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 2.公共字串.py


# 求最长公共字串

s1 = 'asdfhauiwjbabcdfvbaiuasdfaskjdfnlhafnsjxffgsdfsdfknfjkaiweasd,fnkanfkkafsefd'
s2 = 'aklsnfuinvjasdfkkalksnfoefnasdkfnasdfxnusdfsdfsdfsdfabcihvuzcjkniewu'



#### 矩阵算法

s2_index = 0
maxth = 0
matrix = []
for i,val1 in enumerate(s1):
    matrix.append([])
    for j,val2 in enumerate(s2):
        if val1 != val2:
            matrix[i].append(0)
        else:
            if i == 0 or j == 0:
               matrix[i].append(1)
            else:
                matrix[i].append(matrix[i-1][j-1] + 1)

            if matrix[i][j] > maxth:
                maxth = matrix[i][j]
                s2_index = j + 1


print(s2[s2_index - maxth:s2_index])

