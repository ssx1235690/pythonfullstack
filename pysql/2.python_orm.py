# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 11:35
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 2.python_orm.py


import  sqlalchemy
from sqlalchemy import  create_engine,Table,MetaData
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
engine_mariadb = create_engine("mysql://root@192.168.157.132/test",echo=False)
print(type(engine_mariadb))
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(6))

    def __repr__(self):
       return "<User(id='%d',name='%s')>" % (
                            self.id,self.name)
class study_record(Base):
    __tablename__ = "study_record"

    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    status = Column(Integer)
    stu_id = Column(Integer,ForeignKey(Student.id))
    def __repr__(self):
        return "<User(id='%d',day='%d',status='%d',stu_id='%d')>" % (
            self.id, self.day, self.status, self.stu_id)
    student = relationship('Student', backref="stu_record")
# 创建数据库
Base.metadata.create_all(engine_mariadb)

# 连接数据库并操作数据

# 创建session class
Session = sessionmaker(bind=engine_mariadb)
#生成 session 对象
session = Session()

student1 = Student(name="xx1")
student2 = Student(name="xx2")
student3 = Student(name="xx3")

study_record1 = study_record(day=1, status=0, stu_id=1)
study_record2 = study_record(day=2, status=1, stu_id=1)
study_record3 = study_record(day=1, status=0, stu_id=2)
study_record4 = study_record(day=2, status=0, stu_id=2)
study_record5 = study_record(day=2,status=0, stu_id=3)
study_record6 = study_record(day=2, status=0, stu_id=3)
study_record7 = study_record(day=2, status=0, stu_id=2)

# session.add_all([student1,student2,student3,study_record1,study_record2,study_record3,study_record4,study_record5
#                  ,study_record6,study_record7])
# session.commit()

res = session.query(Student).filter(Student.name=="xx1").first()

# 查询student 中的记录 可以通过这个方式获得我们的 stu_record 中的内容
print(res.stu_record)