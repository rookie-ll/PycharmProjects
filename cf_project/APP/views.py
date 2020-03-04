from flask import Blueprint
from APP.ext import db
from .models import Class_dd


blue=Blueprint('f_blue',__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/index/')
def index():
    return 'hello'


@blue.route('/createdb/')
def create_db():
    db.create_all()
    return 'ojbk'


@blue.route('/insert/')
def insert():
    c=Class_dd()
    c.username='我日'
    db.session.add(c)
    db.session.commit()
    return 'ojbk'