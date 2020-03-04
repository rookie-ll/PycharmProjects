from APP.ext import db

class Class(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    store_name=db.Column(db.String(30),unique=True)
    phone=db.Column(db.String(11),unique=True)
    phone2=db.Column(db.String(11))
    rem=db.Column(db.String(100))

