from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

db=SQLAlchemy()
migrate=Migrate()

def init_etx(app):
    db.init_app(app=app)
    migrate.init_app(app,db)
    Bootstrap(app)
    DebugToolbarExtension(app)