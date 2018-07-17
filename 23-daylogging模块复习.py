
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 15:43
# @Author  : sxsong
# @Site    : 
# @File    : 23-daylogging模块复习.py
# @Software: PyCharm

import logging
logging.info('this is info message')
logging.debug('this is debug message')
logging.warning('this is warning message')
logging.error('this is error message')
logging.critical('this is critical message')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename=r'c:\user\ronglian\desktop\myapp.log', filemode='w')

logger = logging.getLogger(__name__)
logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')