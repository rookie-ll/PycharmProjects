from datetime import datetime
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=True)
    body = db.Column(db.Text)
    comments = db.relationship("Comment", backref="posts", cascade='all, delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auther = db.Column(db.String(60))
    body = db.Column(db.Text)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    reply_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    replys = db.relationship("Comment", back_populates="replyd", cascade='all, delete-orphan')
    replyd = db.relationship("Comment", back_populates="replys", remote_side=[id])
