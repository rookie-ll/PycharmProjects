from . import blue
#from app import db
from flask import render_template
from .models import Class_d,db



@blue.route('/index/')
def index():
    return 'hello'

@blue.route('/createdb/')
def create_db():
    db.create_all()
    return 'ojbk'

@blue.route('/adddb/')
def app_db():
    c=Class_d('ojbk')
    #c.username='刘亮'
    db.session.add(c)
    db.session.commit()
    return 'ojbk'


@blue.route('/selectdb/')
def select_db():
    shows=Class_d.query.all()
    for i in shows:
        print(i)
    print(type(shows))
    print(shows)

    return render_template('database.html',shows=shows)