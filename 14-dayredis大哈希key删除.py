#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/3/20
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import datetime
table = 'song'
riQi= '2018-02-28'
r = redis.Redis(host='localhost', port=6379,db=13,decode_responses=True,charset='utf8')
result = r.hscan_iter(table,match=None,count=None)
while True:
	try:
		song = next(result)
		k = song[0]
		v = song[1]
		day = v.split(' ')[0]
		day = datetime.datetime.strptime(day,"%Y-%m-%d")
		strftime = datetime.datetime.strptime(riQi, "%Y-%m-%d")
		if day < strftime:
			print(song)
	except StopIteration as song:
		print("Generator return value: %s " % song.value)
		break
#result = r.hscan('webpage_urls',cursor=0,match=None,count=None)
#for k,v in result[1].items():
#	#k = k.decode('utf8')
#	#v = v.decode('utf8')
#	nv = int(v)
#	print(v)
#	day = v.split(' ')[0]
#	if day < "2018-02-20":
#		print(k)
