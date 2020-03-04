from APP.ext import db


class Class_one(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(15),nullable=True)

    c_by_s=db.relationship('Student_jsj',backref='class_one')

class Student_jsj(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(10))
    age=db.Column(db.Integer)
    tel=db.Column(db.String(11))
    c_id=db.Column(db.Integer,db.ForeignKey('class_one.id'),nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(10),nullable=False)


