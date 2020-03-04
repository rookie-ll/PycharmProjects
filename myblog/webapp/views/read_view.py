from flask import render_template, request, abort, redirect, url_for, flash

from webapp.extends import db
from . import blog_read
from webapp.models import Post, Comment
from webapp.forms import CommentForm, ReplyForm
from flask_login import current_user


@blog_read.route("/", methods=["GET", "POST"])
def blog_read_index():
    comment_form = CommentForm()
    reply_form = ReplyForm()
    pid = request.args.get("id", type=int)
    page = request.args.get("page", 1, type=int)
    if not id:
        raise abort(404)
    post = Post.query.filter(
        Post.id == pid
    ).first()
    if post is None:
        raise abort(404)
    comment_page = Comment.query.filter(
        Comment.post_id == pid
    ).paginate(page=page, per_page=10)

    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            data = comment_form.data.get("textfeild")
            comment = Comment(
                body=data,
                post_id=pid,
                user_id=1
            )
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for("blog_read.blog_read_index", id=pid))
        else:
            flash("请先登陆")
    if reply_form.validate_on_submit():
        if current_user.is_authenticated:
            data = reply_form.data.get("reply")
            cid = request.form.get("remarkId")
            comment=Comment(
                body=data,
                post_id=pid,
                user_id=1,
                reply_id=cid
            )
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for("blog_read.blog_read_index", id=pid))
        else:
            flash("请先登陆")
    return render_template("read.html", comment_form=comment_form, reply_form=reply_form, post=post,
                           page_data=comment_page)
