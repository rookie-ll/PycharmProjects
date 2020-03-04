from faker import Faker
from random import randint

from sqlalchemy.exc import IntegrityError

from APP.extends import db
from APP.models import Class17, Teacher, Student

fake = Faker()


def add_class():

    class17 = Class17(
        name="计算机科学与技术",
        class_num=1
    )
    db.session.add(class17)
    db.session.commit()



def add_student():
    for i in range(10):
        student = Student(
            name=fake.word(),
            age=randint(18,20),
            class_id=1
        )
        db.session.add(student)
    db.session.commit()


def add_teacher():
    for i in range(10):
        teacher = Teacher(
            name=fake.word(),
            age=randint(25,50)
        )
        db.session.add(teacher)
    db.session.commit()
