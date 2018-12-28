#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 10:58
# @Author  : sxsong
# @Site    : 
# @File    : 33-day-web框架入门.py
# @Software: PyCharm

# python地址http://www.cnblogs.com/yuanchenqi/articles/6083427.html


from wsgiref.simple_server import make_server


def f1(req):
    print(req)
    print(req["QUERY_STRING"])

    f1=open("index1.html","rb")
    data1=f1.read()
    return [data1]

def f2(req):

    f2=open("index2.html","rb")
    data2=f2.read()
    return [data2]

import time

def f3(req):        #模版以及数据库

    # f3=open("index3.html","rb")
    # data3=f3.read()
    data3=''
    times=time.strftime("%Y-%m-%d %X", time.localtime())
    data3=data3.replace("",str(times))
    data3=data3.encode('utf8')


    return [data3]


def routers():

    urlpatterns = (
        ('/yuan',f1),
        ('/alex',f2),
        ("/time",f3),
    )
    return urlpatterns


def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])


    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]

httpd = make_server('', 8080, application)

print('Serving HTTP on port 8080...')

# 开始监听HTTP请求:

httpd.serve_forever()