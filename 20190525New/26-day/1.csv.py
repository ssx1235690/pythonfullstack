# -*- coding: utf-8 -*-
<<<<<<< Updated upstream
# @Time    : 2019/8/8 23:48
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : 1.csv.py

import csv

with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
=======
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

>>>>>>> Stashed changes
