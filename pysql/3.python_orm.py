# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:13
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 3.python_orm.py

#### describe   多对多映射
import  sqlalchemy
from sqlalchemy import  create_engine,Table,MetaData
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,DATE
from sqlalchemy.orm import sessionmaker, relationship
engine_mariadb = create_engine("mysql://root@192.168.157.132/test",echo=False)
print(type(engine_mariadb))
Base = declarative_base()

book_m2m_user = Table('book_m2m_user',Base.metadata,
                      Column('book_id',Integer,ForeignKey('book.id')),
                      Column('user_id',Integer,ForeignKey('User.id'))
)
class User(Base):
    __tablename__ = 'User'
    id= Column(Integer,primary_key=True)
    name = Column(String(6))

    def __repr__(self):
       return "<User(id='%d',name='%s')>" % (
                            self.id,self.name)

class book(Base):
    __tablename__ = 'book'
    id= Column(Integer,primary_key=True)
    name = Column(String(6))
    pub_time = Column(DATE)
    users = relationship('User',secondary=book_m2m_user,backref='books')
    def  __repr__(self):
        return  "self.name"


Base.metadata.create_all(engine_mariadb)

u1 = User(name='sxsong')
u2 = User(name='lele')
u3 = User(name='qing')

book1 = book(name='lele ai baba',pub_time='2016-10-01')
book2 = book(name='lele ai mama',pub_time='2016-10-01')

book1.users= [u1,u2]
book2.users= [u1,u2,u3]

Session = sessionmaker(bind=engine_mariadb)
#生成 session 对象
session = Session()

session.add_all([u1,u2,u3,book1,book2])
session.commit()

