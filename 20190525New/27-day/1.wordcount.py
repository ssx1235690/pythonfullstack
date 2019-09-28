# -*- coding: utf-8 -*-
# @Time    :  2019/8/19 10:07
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.wordcount.py


import re


Str = '''
You were my conscience, so silent now you’re like water
And we started drowning, not like we’d sink any farther.
But I let my heart go, it’s somewhere down the bottom.
But I’ll get a new one, come back from the hope that you’ve stolen.
I’ll stop the whole world, I’ll stop the whole world
From turning into a monster, and eating us alive
Don’t you ever wonder how we survive?
Well now that your gone, the world is ours.
I’m only human, I’ve got a skeleton in me
but I’m not the villain, despite what you’re always preaching.
Call me a traitor, I’m just collecting your victims
And they’re getting stronger
I hear them calling.
I’ll stop the whole world, I’ll stop the whole world
From turning into a monster, and eating us alive
Don’t you ever wonder how we survive?
Well now that your gone, the world is ours.
Well you thought of straight solutions
that I liked the attention
And not always knowing the answers
You’re gonna lose it 
You’re gonna lose it
I’ll stop the whole world, I’ll stop the whole world
From turning into a monster, and eating us alive
Don’t you ever wonder how we survive?
Well now that your gone, the world is ours
'''

word_dict = {}
def makekeys(strxx):
    strxx = strxx.lower()
    flag = 0
    for i in range(len(strxx)):

        if flag == 0:
            start = i

        if  re.match('\w',strxx[i]):
            flag = 1
            continue
        elif  re.match('\W',strxx[i]) and re.match('\w',strxx[i-1]):
            key = strxx[start:i]
            if not  key in word_dict.keys():
                word_dict[key] = 0
            else:
                word_dict[key] += 1
            flag = 0
        i += 1
    return  word_dict




def wordcount(strxxx):
    """
    进行词量统计的一个函数
    原理  分词 ---- 组词典 -----sort  ---返回 top5
    :return:
    """
    result = makekeys(strxxx)
    print(result)
    sorted_result = sorted(result,key = lambda x:result[x],reverse=True)
    for i in range(5):
        print(sorted_result[i],result[sorted_result[i]])


wordcount(Str)


