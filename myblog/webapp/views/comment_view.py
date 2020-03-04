from flask import render_template, request, redirect, url_for, flash
from . import comment
from webapp.models import Message
from webapp.extends import db
from flask_login import current_user


@comment.route("/", methods=["GET", "POST"])
def comment_index():
    page = request.args.get("page", 1, type=int)
    msg_page = Message.query.order_by(
        Message.timestamp.desc()
    ).paginate(page=page, per_page=20)

    if request.method == "GET":
        return render_template("message.html", msg_page=msg_page)
    if request.method == "POST":
        if current_user.is_authenticated:
            com = request.form.get("editorContent")
            reply = request.form.get("replyContent")
            if com:
                msg = Message(
                    body=com,
                    user_id=1,
                )
                db.session.add(msg)
                db.session.commit()
                return redirect(url_for("comment.comment_index"))
            if reply:
                rid = request.form.get("targetUserId", type=int)
                print(reply)
                print(rid)
                if rid:
                    msg = Message(
                        body=reply,
                        user_id=2,
                        reply_id=rid
                    )
                    db.session.add(msg)
                    db.session.commit()
                    return redirect(url_for("comment.comment_index"))
        else:
            flash("请先登陆再来评论","err")
    return render_template("message.html", msg_page=msg_page)
