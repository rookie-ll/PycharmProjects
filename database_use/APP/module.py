from APP.ext import db
from datetime import datetime


class Base(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    updata_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


# 多对多辅助表
tags = db.Table("tags",
                db.Column("crouse_id", db.Integer, db.ForeignKey("crouse.id"), primary_key=True),
                db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True)
                )


class Xclass(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(30), unique=True, nullable=True)
    student = db.relationship("Student", backref="xclass", cascade='all, delete-orphan')

    def __repr__(self):
        return "<Xclass %r>" % Xclass.class_name


class Crouse(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crouse_name = db.Column(db.String(50), unique=True, index=True, nullable=True)
    student = db.relationship("Student", secondary="tags", back_populates="crouse")

    def __repr__(self):
        return "<Crouse %r>" % Crouse.crouse_name


class Student(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(20), nullable=True)
    student_id = db.Column(db.Integer, index=True, unique=True, nullable=True)
    class_id = db.Column(db.Integer, db.ForeignKey("xclass.id"))
    crouse = db.relationship("Crouse", secondary="tags", back_populates="student")

    def __repr__(self):
        return "<Student %r>" % Student.student_name
