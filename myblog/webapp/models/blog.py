from datetime import datetime

from webapp.extends import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    posts = db.relationship("Post", back_populates="category")

    def delete(self):
        default_category = Category.query.get(1)
        posts = self.posts[:]
        for post in posts:
            post.category = default_category
            db.session.delete(self)
            db.session.commit()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    summary = db.Column(db.Text)
    body = db.Column(db.Text)
    orig = db.Column(db.Boolean, default=False)
    sticky = db.Column(db.Boolean, default=False)
    page_views = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    category = db.relationship("Category", back_populates="posts")
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reply_id = db.Column(db.Integer, db.ForeignKey("comment.id"))

    post = db.relationship("Post", back_populates="comments")
    user = db.relationship("User", back_populates="comments")

    replies = db.relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])

# class Reply(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#
#     comment_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#
#     comment = db.relationship("Comment", back_populates="replies")
#     user = db.relationship("User", back_populates="replies")
