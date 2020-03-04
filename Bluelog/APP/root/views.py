import random

from flask_admin import expose, BaseView

from APP.me_models import Category, Admin
from . import adm
from APP.ext import admins, db


@adm.route('/')
def index():
    ls=Category.query.get(random.randint(1, Category.query.count()))
    print(type(ls))
    print(str(ls))

    return "hello root"

class MyView(BaseView):

    # 这里类似于app.route()，处理url请求

    @expose('/')
    def index(self):
        return self.render('index.html')


admins.add_view(MyView(name=u'Hello'))

from flask_admin.contrib.sqla import ModelView

# 在这里初始化Flask Flask-SQLAlchemy Flask-Admin

admins.add_view(ModelView(Admin, db.session))