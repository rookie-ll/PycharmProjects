from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
def create_ext(app):
    db.init_app(app)