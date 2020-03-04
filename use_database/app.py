from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/XK"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "False"
app.config['SQLALCHEMY_BINDS']="mysql+pymysql://root:123456@127.0.0.1:3306/test3"
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

tags = db.Table("tags",
                db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
                db.Column("teacher_id", db.Integer, db.ForeignKey("teacher.id"))
                )


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    #age=db.Column(db.Integer)
    teachers = db.relationship("Teacher", secondary=tags, backref=db.backref("students", lazy="dynamic"),
                               lazy="dynamic")
    # teachers = db.relationship("Teacher", secondary=tags, back_populates="students")


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    #age=db.Column(db.Integer)
    # students = db.relationship("Student", secondary=tags, back_populates="teachers")


@app.route('/add_teacher/')
def hello_world():
    teacher = Teacher(name="数学老师")
    db.session.add(teacher)
    db.session.commit()
    return 'add_teacher'


@app.route('/add_student/')
def hello_word2():
    student = Student(name="数学老师的学生")
    db.session.add(student)
    db.session.commit()
    return "add_student"


@app.route('/add_tags/')
def tags():
    teacher = Teacher.query.filter_by(name="数学老师").first()
    studetn = Student.query.filter_by(name="数学老师的学生").first()
    student2 = Student.query.get(2)
    # teacher.students.append(studetn)
    # studetn.teachers.append(teacher)
    teacher.students.append(student2)
    db.session.add(teacher)
    # db.session.add(studetn)
    db.session.commit()

    return "ok"


@app.route('/show_database2/')
def database2():

    return 'ok'

@app.route('/show_data')
def show_data():
    teacher = Teacher.query.filter_by(name="数学老师").first()
    studetn = Student.query.filter_by(name="数学老师的学生").first()
    print(teacher.students)
    return "show data is ok"


@app.route('/')
def index():
    return "hello "


if __name__ == "__main__":
    manager.run()
