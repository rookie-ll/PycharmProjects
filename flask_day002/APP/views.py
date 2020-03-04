import random
from redis import StrictRedis

from flask import Blueprint, render_template, redirect, current_app, request,Response,session,url_for

from APP.ext import db
from APP.models import Student_jsj, Class_one, User

blue=Blueprint('f_blue',__name__,template_folder='../templates')
def init_blue(app):
    app.register_blueprint(blueprint=blue)

sr=StrictRedis()

@blue.route('/index/')
def index():
    configs=current_app.config
    print(type(configs))
    print(configs)
    for key in configs.keys():
        print(key,configs.get("key"))
        print("...............................")
    return  render_template('config.html')


@blue.route('/createclass/')
def create_class():
    clas=Class_one()
    clas.name="17计算机本科班"
    db.session.add(clas)
    db.session.commit()

    return 'ojbk'


@blue.route('/createstudent/')
def create_student():
    num=random.randrange(100)
    num2=random.randrange(10)
    student=Student_jsj()
    cla=Class_one.query.order_by(Class_one.id.desc()).first()
    student.name='流量%d'%num
    student.age=12+num2
    student.tel=12312312312
    student.c_id=cla.id
    db.session.add(student)
    db.session.commit()
    return 'ojbk'

@blue.route('/page/')
def pagelist():
    page=request.args.get("page",1,type=int)
    per_page=request.args.get("page",4,type=int)
    student=Student_jsj.query.paginate(page,per_page)
    return render_template('pagelist.html',student=student)


@blue.route('/addadmin/')
def add_admin():
    names=request.form.get("username")
    if names==User.query.filter(User.username==names):
        return "xjbt"
    else:
        user=User()
        user.password=123123
        user.username="老李"
        db.session.add(user)
        db.session.commit()
        return 'ojbk'


@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password",type=int)
        a=User.query.filter(User.username==username).first().username
        b=User.query.filter(User.password==password).first()
        print(type(a))
        print(a)
        print(type(b))
        print(b)
        if username==User.query.filter(User.username==username).first().username and password==User.query.filter(User.password==password).first().password:

            rest=Response(response="hello word%s"%username)
            #rest.set_cookie("username",username)
            session["username"] = username
            return rest
        else:
            return "别特码瞎鸡巴填"

@blue.route('/home/')
def home():
    #username=request.cookies.get("username")
    username=session.get("username")
    hello="hello %s"%username
    return render_template('home.html',hello=hello)

@blue.route('/unlogin/')
def un_login():
    delse=redirect(url_for("f_blue.home"))
    #delse.delete_cookie("username")
    session.pop("username")
    return delse

@blue.route('/rediss/')
def redis_s():
    student=sr.get("student1")
    class2=sr.hget("class2","yy")
    keyss=sr.keys("*")
    r=Response("hello%s,%s,%s"%(student,class2,keyss))
    return r