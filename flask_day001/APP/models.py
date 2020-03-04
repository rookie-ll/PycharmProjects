from APP.etx import db


class Student(db.Model):
    #__tablename__='student'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(33))
    #num=db.Column(db.Integer)

class Hello(db.Model):
    #__tablename__="hello"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(22))

class Grade(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(19),unique=True)
    g_student=db.relationship('Students',backref='grade',lazy=True)#lazy惰性加载


class Students(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name=db.Column(db.String(20))
    s_age=db.Column(db.Integer,default=16)
    g_id=db.Column(db.Integer,db.ForeignKey("grade.id"),nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),nullable=True)
    password=db.Column(db.String(30),nullable=True)

