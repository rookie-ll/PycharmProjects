import random

from flask import Blueprint,render_template,request,redirect,url_for
from sqlalchemy import and_, or_

from APP.models import Student, Grade, Students, User
from APP.etx import db

blue = Blueprint("f_blue",__name__)

def create_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return redirect(url_for('f_blue.login_for_cookies'))

@blue.route('/createdb/')
def create_tb():
    db.create_all()
    return 'create ojbk'

@blue.route('/addstudent/')
def adds():
    s=Student()
    num=random.randrange(100)
    s.name="小边与飞%s"%num
    db.session.add(s)
    db.session.commit()

    return 'ojbk'

@blue.route('/getstudent/')
def getstu():
    s=Student.query.all()
    print(s)
    for i in s:
        print(i)
    return render_template('index.html',student=s)

@blue.route('/setstudent/')
def setstu():
    s=Student.query.first()
    s.name = '老边滚出去了'
    db.session.add(s)
    db.session.commit()
    return '老边已经滚出去了'

@blue.route('/delstudent/')
def dlstu():
    s=Student.query.first()
    db.session.delete(s)
    db.session.commit()
    return '老边已经被删除了'

@blue.route('/getlb/')
def get_l():
    #s=Student.query.filter(Student.name.contains("旗"))
    #s = Student.query.filter_by(id=20)
    #s = Student.query.order_by('id')
    #student = Student.query.order_by('id').offset(3).limit(3)
    #student = Student.query.filter(and_(Student.id<11,Student.id>9))
    student = Student.query.filter(or_(Student.id < 11, Student.id > 9))
    return render_template('lb.html',students=student)

@blue.route('/getstudent2/')
def get_2():
    #student=Student.query.order_by(Student.id.desc()).first()
    student = Student.query.order_by(db.desc(Student.id)).first()
    students=Student.query.get(10)
    print(student)
    print(students)
    return 'ojbk'

@blue.route('/page/')
def per_page():
    page=request.args.get("page",1,type=int)
    print(page)
    print(type(page))
    per_pages=request.args.get("per_pages",3,type=int)
    student=Student.query.limit(per_pages).offset((page - 1) * per_pages)
    return render_template('lb.html',students=student)


@blue.route('/getpaginate/')
def get_pagi():
    page = request.args.get("page", 1, type=int)
    per_pages = request.args.get("per_pages", 4, type=int)
    paginates=Student.query.paginate(page,per_pages)

    return render_template('pagelist.html',students=paginates,per_page=per_pages)

@blue.route('/addgrade/')
def add_grade():
    grade=Grade()
    num=random.randrange(100)
    grade.name="１７计算机本科(%d)班"%num
    db.session.add(grade)
    db.session.commit()
    return 'grade add success'

@blue.route('/addstudents/')
def add_students():
    grade=Grade.query.order_by(Grade.id.desc()).first()
    student=Students()
    num=random.randrange(100)
    num2=random.randrange(10)
    student.s_age = num+num2
    student.s_name = '流量%d'%num
    student.g_id = grade.id

    db.session.add(student)
    db.session.commit()

    return 'ojbk'

@blue.route('/getstudentbygrade/')
def get_s_by_g():
    student=Students.query.order_by(Students.id.desc()).first()
    #grade=Grade.query.get(student.g_id)
    print(student.grade)
    grade=student.grade
    return "hello %s" %grade.name

@blue.route('/getgradebystudent')
def get_g_by_s():
    grade=Grade.query.first()
    print(type(grade.g_student))
    print(grade.g_student)
    student=grade.g_student
    #student=Students.query.filter(Students.g_id==grade.id)
    #print(student)
    return render_template('studentlist.html',students=student)


@blue.route('/zc/',methods=['GET','POST'])
def zc():
    user=User()
    user.username="老李"
    user.password="laoli123"
    db.session.add(user)
    db.session.commit()
    return '添加完成'

@blue.route('/login1/',methods=['GET','POST'])
def login_for_cookies():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        a=User.query.filter(User.username==username).all()
        b=User.query.filter(User.password==password).all()
        print(a[0].username)
        print(b[1].password)

        if username==User.query.filter(User.username==username).first().username and password==User.query.filter(User.password==password).first().password:
            return 'ojbk'
        else:
            return '瞎鸡巴填'