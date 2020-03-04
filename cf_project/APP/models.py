from APP.ext import db

class Class_dd(db.Model):
    __tablename__="mdzz"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(18))

