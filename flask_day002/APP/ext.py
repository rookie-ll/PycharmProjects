from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CSRFProtect
from flask_session import Session


db=SQLAlchemy()
migrate=Migrate()
toolbar=DebugToolbarExtension()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    toolbar.init_app(app)
    #CSRFProtect.init_app(app)
    #Session.init_app(app)
