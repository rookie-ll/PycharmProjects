from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_migrate import Migrate

db = SQLAlchemy()
admin = Admin()
migrate = Migrate()


def app_extend(app):
    db.init_app(app)
    admin.init_app(app,
                   index_view=AdminIndexView(
                       name='Home',
                       template='index.html',
                       url='/admin'
                   )
                   )
    migrate.init_app(app, db)
