from flask import Blueprint
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from APP import db
from APP.extends import admin
from APP.models import Class17, Teacher, Student

admin_blue = Blueprint('admin_blue', __name__)


def app_blueprints(app):
    app.register_blueprint(admin_blue)


class Myviews(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


#admin.add_view(Myviews(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(Myviews(name='Test'))
admin.add_view(ModelView(Class17, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Teacher, db.session))


@admin_blue.route('/')
def index():
    return "hello admin"


@admin_blue.route('/add_class17/')
def add_class17():
    for i in range(1, 5):
        class_17 = Class17.query.filter(Class17.id == 3).first()
        teacher = Teacher.query.filter(Teacher.id == i).first()
        print(teacher.class17s)
        teacher.class17s.append(class_17)
        db.session.add(teacher)
    db.session.commit()
    return "ok"


@admin_blue.route('/add_student/')
def add_student():
    for i in range(1, 5):
        student = Student.query.filter(Student.id == i).first()
        teacher = Teacher.query.filter(Teacher.id == i).first()
        student.teachers.append(teacher)
        db.session.add(student)
    db.session.commit()
    return "ok"


@admin_blue.route('/add_class/')
def add_class():
    class_17 = Class17(
        name="17计算机科学与技术",
        class_num=2
    )
    db.session.add(class_17)
    db.session.commit()
    return "ok"
