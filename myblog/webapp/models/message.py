from datetime import datetime

from webapp.extends import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reply_id = db.Column(db.Integer, db.ForeignKey("message.id"))

    replies = db.relationship("Message", back_populates="replied", cascade='all, delete-orphan')
    replied = db.relationship("Message", back_populates="replies", remote_side=[id])
    user = db.relationship("User", back_populates="messages")
