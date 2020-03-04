from APP.app_blue import app_blue
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView

from APP.ext import adm
from APP.models import Admin, Comment, Category, Link, Post, db

# from flask import Blueprint

# admin_blue = Blueprint('app_blue', __name__, template_folder='../../templates/app_blue')
#
#
# def create_blue(app):
#     app.register_blueprint(admin_blue, url_prefix='/app_blue')


@app_blue.route('/')
def indexs():
    return "hello app_blue"


class MyViews(BaseView):

    # 这里类似于app.route()，处理url请求

    @expose('/')
    def index(self):
        return self.render('adm/index.html')


adm.add_view(MyViews(name='Hello'))

# 在这里初始化Flask Flask-SQLAlchemy Flask-Admin

adm.add_view(ModelView(Admin, db.session))
adm.add_view(ModelView(Category, db.session))
adm.add_view(ModelView(Comment, db.session))
adm.add_view(ModelView(Link, db.session))
adm.add_view(ModelView(Post, db.session))