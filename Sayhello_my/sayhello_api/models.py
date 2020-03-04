from sayhello_api.ext import db
from datetime import datetime


class Base():
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)


class Message(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
