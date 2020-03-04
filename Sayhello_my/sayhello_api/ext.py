from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()
debugtool = DebugToolbarExtension()


def insert_ext(app):
    db.init_app(app=app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    moment.init_app(app)
    debugtool.init_app(app)
