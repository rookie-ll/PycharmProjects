from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap
from flask_admin import Admin
db = SQLAlchemy()
#bootstrap = Bootstrap()
admins=Admin()


def create_ext(app):
    db.init_app(app)
    #bootstrap.init_app(app)
    admins.init_app(app)