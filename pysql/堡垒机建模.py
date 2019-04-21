# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 22:09
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 堡垒机建模.py


from pysql import setting
from sqlalchemy import  create_engine,Table,MetaData
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Enum, Integer, String,ForeignKey,UniqueConstraint
import sys
from  sqlalchemy.orm import  relationship
print(sys.path)

mysql_engine = setting.engine_mariadb
Base = declarative_base()

host_m2m_remote_user = Table('host_m2m_remote_user',Base.metadata,
                             Column('host_id',Integer,ForeignKey('host.id')),
                             Column('remote_user_id',Integer,ForeignKey('remote_user.id'))
                             )

class Host(Base):
    __tablename__ = 'Host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer)
    remote_users = relationship('remote_user',host_m2m_remote_user,backref='hosts')
    def __repr__(self):
        return 'hostname: {1}, ip {2}, port: {3}'.format(self.hostname,self.ip,self.port)

class Remote_user(Base):
    __tablename__ = 'Remote_user'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True)
    password = Column(String(64))
    auth_type = Column(Enum(0,1))
    __table_args__ = (UniqueConstraint('username','password','auth_type',name='sssssss'))
    def __repr__(self):
        return 'username: {1}, password {2}'.format(self.username,self.password)


class User_profile(Base):
    __tablename__ = 'User_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True)
    password = Column(String(64))

    def __repr__(self):
        return 'username: {1}'.format(self.username)

