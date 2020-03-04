from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap=Bootstrap()


def init_etx(app):
    db.init_app(app=app)
    bootstrap.init_app(app=app)
