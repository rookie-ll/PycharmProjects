from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#链接数据库e
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/lianxi'
#跟踪２
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#显示ｓｑｌ语句
app.config['SQLALCHEMY_ECHO'] = True

db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='tab_role'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    users=db.relationship("User",backref="role")

class User(db.Model):
    __tablename__='tab_user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    email=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(18))
    role_id=db.Column(db.Integer,db.ForeignKey("tab_role.id"))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    r=Role(name="admin")
    db.session.add(r)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=r.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=r.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=r.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=r.id)

    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()
