# from flask_admin import BaseView, expose
# from flask_admin.contrib.sqla import ModelView
#
# from APP.ext import adm
# from APP.models import Admin, Category, Comment, Link, Post, db
#
#
# class MyViews(BaseView):
#
#     # 这里类似于app.route()，处理url请求
#
#     @expose('/')
#     def index(self):
#         return self.render('adm/index2.html')
#
#
# adm.add_view(MyViews(name='Hello'))
#
# # 在这里初始化Flask Flask-SQLAlchemy Flask-Admin
#
# adm.add_view(ModelView(Admin, db.session))
# adm.add_view(ModelView(Category, db.session))
# adm.add_view(ModelView(Comment, db.session))
# adm.add_view(ModelView(Link, db.session))
# adm.add_view(ModelView(Post, db.session))
