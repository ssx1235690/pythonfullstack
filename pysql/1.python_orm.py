# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 9:30
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.python_orm.py


import  sqlalchemy
from sqlalchemy import  create_engine,Table,MetaData
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

print(sqlalchemy)
### 建立连接
engine_mariadb = create_engine("mysql://root@192.168.157.132/test",echo=True,encoding='utf8')
print(type(engine_mariadb))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(6))
    fullname = Column(String(64))
    nickname = Column(String(128))

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

# lll=User()
# print(lll) 输出资料
# print(User.__table__)

# 创建数据库
Base.metadata.create_all(engine_mariadb)

# 连接数据库并操作数据
from sqlalchemy.orm import sessionmaker
# 创建session class
Session = sessionmaker(bind=engine_mariadb)
#生成 session 对象
session = Session()

#创建 插入语句
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
# 输入有误还可以执行回滚
session.rollback()
# 执行提交
session.commit()


# 使用查询语句  filter_by  和  filter 是有区别的
data = session.query(User).filter_by(name='ed').all()
print(data[0])
#数据修改
data[0].fullname='good boy'
# 由于没有对 操作进行 commit 所以真实数据并没有改变只是再这个 session的缓存中这个数据显示为此。

data = session.query(User).filter(User.id>0).all()
print(data)



metadata = MetaData()
city = Table('city', metadata, autoload=True, autoload_with=engine_mariadb)
country = Table('country', metadata, autoload=True, autoload_with=engine_mariadb)
countrylanguage = Table('countrylanguage', metadata, autoload=True, autoload_with=engine_mariadb)
res = session.query(city).all()
print(res[0])

res = session.query(city,country).all()
print(res[1])