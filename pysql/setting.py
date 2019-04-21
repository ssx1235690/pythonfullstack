# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 22:12
# @Author  : songxy
# @Email   : 2953xx998@qq.com
# @File    : setting.py

import  sqlalchemy
from sqlalchemy import  create_engine,Table,MetaData
import pymysql
pymysql.install_as_MySQLdb()

print(sqlalchemy)
### 建立连接
engine_mariadb = create_engine("mysql://root@192.168.157.132/test",echo=True,encoding='utf8')