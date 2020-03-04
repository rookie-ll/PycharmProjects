from datetime import datetime
from webapp.extends import db
from itsdangerous.jws import TimedJSONWebSignatureSerializer as serializer
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.extends import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    emial = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text(100))
    face = db.Column(db.String(255))  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)

    userloges = db.relationship("Userlog", backref="user")
    posts = db.relationship("Post", back_populates="user", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="user", cascade="all, delete-orphan")  # 评论的反向关系
    messages = db.relationship("Message", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Userlog %r>" % self.username

    @property
    def password(self):
        raise ArithmeticError("password是不可读字段")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if self.password_hash:
            return check_password_hash(self.password_hash, password)
        else:
            return False


# 会员登陆日志
class Userlog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Userlog %r>" % self.id


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))
