# -*- coding: utf-8 -*-
# @Time    :  2019/7/13 20:32
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.字典扁平化.py



# 源字典  {‘a’:{‘b’:1,‘c’:2},‘d’:{‘e’:3,‘f’:{‘g’:4}}}
# 目标字典   {'d.e': 3, 'a.c': 2, 'd.f.g': 4, 'a.b': 1}


source_dict = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

target_dict = {}

def flat(xxx,prefix=''):
    for k,v in xxx.items():
        if isinstance(v,dict):
            prefix += k+'.'
            flat(v,prefix=prefix)
        else:
            k = prefix + k
            target_dict[k] = v

    return target_dict
print(flat(source_dict),'xxxxxx',source_dict)


