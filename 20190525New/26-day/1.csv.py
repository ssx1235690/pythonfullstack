# @Time    :  2019/8/3 11:30
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.csv.py

from pathlib import  Path

import  csv


p = Path('./test.csv')


with open('./test.csv','r',newline='') as song_cvs:
    spamer = csv.reader(song_cvs, delimiter=' ', quotechar='|')
    for i in spamer:
        print(','.join(i))


p.parent.mkdir(parents=True,exist_ok=True)


headers = ['class','name','sex','height','year']

rows = [
        {'class':1,'name':'xiaoming','sex':'male','height':168,'year':23},
        {'class':1,'name':'xiaohong','sex':'female','height':162,'year':22},
        {'class':2,'name':'xiaozhang','sex':'female','height':163,'year':21},
        {'class':2,'name':'xiaoli','sex':'male','height':158,'year':21},
    ]

with open('./test.csv','w',newline='')as f:
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)