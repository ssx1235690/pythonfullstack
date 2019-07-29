# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 22:49
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.configparser.py

import configparser


src = 'php.ini'
dst = 'php.json'
cfg = configparser.ConfigParser()
cfg.read(src)


d = {}
for k,v in  cfg.items():
    d[k] = dict(cfg.items(k))
print(d)
import  json


with open(dst,'w') as song:
    json.dump(d,song,indent=4)