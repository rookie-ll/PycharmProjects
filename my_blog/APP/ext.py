from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
from flask_admin import Admin, AdminIndexView

db = SQLAlchemy()
# bootstrap = Bootstrap()
adm = Admin()


def create_ext(app):
    db.init_app(app)
    adm.init_app(app,
                   index_view=AdminIndexView(
                       name='Home',
                       template='/adm/index.html',
                       url='/admin'
                   )
                   )

    # bootstrap.init_app(app)
