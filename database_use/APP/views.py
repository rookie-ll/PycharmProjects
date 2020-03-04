from flask import Blueprint
from APP.module2 import Post, Comment, Category, Admin
from APP.ext import db
from APP.module import Crouse, Xclass, Student, tags

api = Blueprint("api", __name__)


def create_blue(app):
    app.register_blueprint(api)


@api.route("/")
def index():
    return "hello"


@api.route("/add_comment")
def add_comment():
    comment=Comment(
        author="老李",
        email="123123@qq.com",
        site="站点?",
        body="俺是一个老李的评论",
        reviewed=True,
        post_id=1,
    )
    db.session.add(comment)
    db.session.commit()
    return "hello ok"


@api.route("/reply_comment")
def reply():
    comment=Comment(
        author="老王",
        email="123123@qq.com",
        site="站点?",
        body="俺是一个回复,回复老李的",
        reviewed=True,
        post_id=1,
        replied_id=12
    )
    db.session.add(comment)
    db.session.commit()
    return "hello ok"


@api.route("/del_com")
def del_com():
    ids=1
    id=Comment.query.filter_by(id=ids).first()
    db.session.delete(id)
    db.session.commit()
    return "del ok"


@api.route("/add_admin")
def admin():
    admins = Admin(
        username="老王",
        password="123123",
        blog_title="标题",
        blog_sub_title="噩噩噩",
        name="sdfsfs",
        about="的看风景啊缩略法"
    )
    db.session.add(admins)
    db.session.commit()
    return "hello"


@api.route("/category/")
def category():
    cat = Category(
        name="第一类"
    )
    db.session.add(cat)
    db.session.commit()
    return "ok"


@api.route("/ljlb/")
def ljlb():
    ids = Category.query.filter_by(id=1).first()
    post = Post(
        title="我的梦2",
        body="emmmmmmmmmmmmmmmm我没有梦sdfdsfs",
        category_id=ids.id
    )
    db.session.add(post)
    db.session.commit()
    return "ok"


@api.route("/del_post")
def del_post():
    id=Post.query.filter_by(id=1).first()
    db.session.delete(id)
    db.session.commit()
    return "def ok"

@api.route("/add_class/")
def add_class():
    xclass = Xclass(class_name="17计算机科学与技术(2)")
    db.session.add(xclass)
    db.session.commit()
    return "addclass is ok"


@api.route("/add_crouse/")
def add_crouse():
    crouse = Crouse(crouse_name="数学")
    db.session.add(crouse)
    db.session.commit()
    return "addcrouse is ok"


@api.route("/add_student/")
def add_student():
    student = Student(student_name="流量", student_id=1234567894, class_id=3)
    db.session.add(student)
    db.session.commit()
    return "addclass is ok"


@api.route("/add_tags/")
def del_data():
    data = Xclass.query.filter(Xclass.id == 1).first()
    crouse = Crouse.query.filter(Crouse.id == 1).first()
    crouse2 = Crouse.query.filter(Crouse.id == 2).first()
    studet = Student.query.filter(Student.id == 2).first()
    student2 = Student.query.filter(Student.id == 1).first()

    print(studet.crouse)
    print(student2.crouse)
    print(crouse.student)
    print(crouse2.student)
    return "tags "


@api.route("/select/")
def select_data():
    data = Xclass.query.filter(Xclass.id == 1).first()
    crouse = Crouse.query.filter(Crouse.id == 1).first()
    crouse2 = Crouse.query.filter(Crouse.id == 2).first()
    studet = Student.query.filter(Student.id == 2).first()
    student2 = Student.query.filter(Student.id == 1).first()
    studet.crouse.append(crouse)
    studet.crouse.append(crouse2)
    student2.crouse.append(crouse)
    db.session.add(studet)
    db.session.add(student2)
    db.session.commit()
    return "%s" % data


@api.route("/add_croouse_student/")
def add_cs():
    student = Student(student_name="张旗", student_id="451515151", class_id=1)
    student2 = Student(student_name="李家慧", student_id="451515156", class_id=1)
    crouse = Crouse(crouse_name="英语")
    crouse2 = Crouse(crouse_name="物理")
    student.crouse.append(crouse)
    student.crouse.append(crouse2)
    student2.crouse.append(crouse)
    student2.crouse.append(crouse2)
    db.session.add(student)
    db.session.add(student2)
    db.session.add(crouse)
    db.session.add(crouse2)
    db.session.commit()
    return "ok"


@api.route('/delclass')
def delclass():
    c=Xclass.query.filter_by(id=2).first()
    db.session.delete(c)
    db.session.commit()
    return "ok"