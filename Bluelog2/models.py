from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .app import app
db=SQLAlchemy(app)



class Base(object):
    add_time = db.Column(db.DateTime, default=datetime.utcnow)


class Admin(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))  # 博客标题
    blog_sub_title = db.Column(db.String(100))  # 博客副标题
    name = db.Column(db.String(30))  # 用户姓名
    about = db.Column(db.Text)  # 关于信息


# 分类
class Category(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)


# 文章
class Post(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    #category = db.Column(db.String(30))
    # timestamp=db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment', backref="post", cascade='all')


class Comment(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))  # 作者
    email = db.Column(db.String(254))  # 电子邮件
    site = db.Column(db.String(255))  # 站点
    body = db.Column(db.Text)  # 正文
    #postr = db.Column(db.String(30))
    from_admin = db.Column(db.Boolean, default=False)  # 是否为管理员评论
    reviewed = db.Column(db.Boolean, default=False)  # 是否通过审核
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    # post = db.relationship("Post", back_populates="comments")

    replied_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    replied = db.relationship("Comment", back_populates="replieds", remote_side=[id])
    replieds = db.relationship("Comment", back_populates="replied", cascade="all")
