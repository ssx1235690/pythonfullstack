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



user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                        Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                        Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                        )
bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup', Base.metadata,
                          Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                          Column('hostgroup_id', Integer, ForeignKey('host_group.id')),
                          )

user_m2m_hostgroup = Table('userprofile_m2m_hostgroup', Base.metadata,
                               Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                               Column('hostgroup_id', Integer, ForeignKey('host_group.id')),
                               )


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    bind_hosts = relationship("BindHost",secondary="bindhost_m2m_hostgroup",backref="host_groups")

    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_type', 'username','password', name='_user_passwd_uc'),)

    id = Column(Integer, primary_key=True)
    AuthTypes = [
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username

class BindHost(Base):
    '''
    192.168.1.11    web
    192.168.1.11    mysql

    '''
    __tablename__ = "bind_host"
    __table_args__ = (UniqueConstraint('host_id','remoteuser_id', name='_host_remoteuser_uc'),)

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    #group_id = Column(Integer,ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))
    host = relationship("Host",backref="bind_hosts")
    #host_group = relationship("HostGroup",backref="bind_hosts")
    remote_user = relationship("RemoteUser",backref="bind_hosts")
    def __repr__(self):
        return "<%s -- %s >" %(self.host.ip,
                                   self.remote_user.username
                                  )

class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))
    bind_hosts = relationship("BindHost", secondary='user_m2m_bindhost',backref="user_profiles")
    host_groups = relationship("HostGroup",secondary="userprofile_m2m_hostgroup",backref="user_profiles")

    def __repr__(self):
        return self.username


# class AuditLog(Base):
#     pass


if __name__ == "__main__":

    Base.metadata.create_all(mysql_engine)  # 创建表结构




##########################自写部分##############################
# host_m2m_remote_user = Table('host_m2m_remote_user',Base.metadata,
#                              Column('host_id',Integer,ForeignKey('host.id')),
#                              Column('remote_user_id',Integer,ForeignKey('remote_user.id'))
#                              )
#
# host_m2m_group = Table('host_m2m_group',Base.metadata,
#                              Column('host_id',Integer,ForeignKey('host.id')),
#                              Column('group_id',Integer,ForeignKey('host_group.id'))
#                              )
#
# class Host(Base):
#     __tablename__ = 'Host'
#     id = Column(Integer,primary_key=True)
#     hostname = Column(String(64),unique=True)
#     ip = Column(String(64),unique=True)
#     port = Column(Integer)
#     remote_users = relationship('remote_user',host_m2m_remote_user,backref='hosts')
#     def __repr__(self):
#         return 'hostname: {0}, ip {1}, port: {2}'.format(self.hostname,self.ip,self.port)
#
#
# class Host_group(Base):
#     __tablename__ = 'Host_group'
#     id = Column(Integer,primary_key=True)
#     groupname = Column(String(64),unique=True)
#     host_id = Column(Integer,ForeignKey(Host.id))
#     host =  relationship('Host',backref='host_group')
#     #多对多关系
#     remote_users = relationship('remote_user', host_m2m_group, backref='group')
#     def __repr__(self):
#         return 'hostname:{0}'.format(self.groupname)
#
# class Remote_user(Base):
#     __tablename__ = 'Remote_user'
#     id = Column(Integer,primary_key=True)
#     username = Column(String(64),unique=True)
#     password = Column(String(64))
#     auth_type = Column(Enum(0,1))
#     #联合唯一索引
#     __table_args__ = (UniqueConstraint('username','password','auth_type',name='sssssss'))
#     def __repr__(self):
#         return 'username: {0}, password {1}'.format(self.username,self.password)
#
#
# class User_profile(Base):
#     __tablename__ = 'User_profile'
#     id = Column(Integer,primary_key=True)
#     username = Column(String(64),unique=True)
#     password = Column(String(64))
#
#     def __repr__(self):
#         return 'username: {0}'.format(self.username)



'''
Base = declarative_base()

user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                        Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                        Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                        )


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_type', 'username','password', name='_user_passwd_uc'),)

    id = Column(Integer, primary_key=True)
    AuthTypes = [
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username

class BindHost(Base):
    # 192.168.1.11    mysql  sh_group

    __tablename__ = "bind_host"
    __table_args__ = (UniqueConstraint('host_id', 'group_id','remoteuser_id', name='_host_group_remoteuser_uc'),)

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    group_id = Column(Integer,ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))
    host = relationship("Host",backref="bind_hosts")
    host_group = relationship("HostGroup",backref="bind_hosts")
    remote_user = relationship("RemoteUser",backref="bind_hosts")
    def __repr__(self):
        return "<%s -- %s --%s>" %(self.host.ip,
                                   self.remote_user.username,
                                   self.host_group.name)

class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))
    bind_hosts = relationship("BindHost", secondary='user_m2m_bindhost',backref="user_profiles")


    def __repr__(self):
        return self.username


class AuditLog(Base):
    pass
'''