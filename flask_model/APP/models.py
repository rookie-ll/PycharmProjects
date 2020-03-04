#from app import db
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def init_db(app):
    db.init_app(app)

class Class_d(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(10))