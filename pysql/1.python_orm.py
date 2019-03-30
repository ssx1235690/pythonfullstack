# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 9:30
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.python_orm.py


import  sqlalchemy
from sqlalchemy import  create_engine
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

print(sqlalchemy)
### 建立连接
engine_mariadb = create_engine("mysql://root@192.168.157.132/song")
print(type(engine_mariadb))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

User.__table__