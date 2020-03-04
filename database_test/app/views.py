from flask import Blueprint, Response, make_response, render_template, request
from sqlalchemy import not_

from app.moels import Post, db, Comment

blue = Blueprint("blue", __name__, template_folder="../templates")


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    page_data = Post.query.paginate(page=page, per_page=5)
    comment_date = Comment.query.order_by(Comment.add_time.desc()).paginate(page=page, per_page=10)
    print(page_data)
    for i in comment_date.items:
        if i.replys:
            print(i.replys)
            for j in i.replys:
                print(j.id)
    # for j in page_data.items:
    #     for i in comment_date.items:
    #         if i.reply_id == None and j.id == i.post_id:
    #             print(i.id)
    # res = [
    #     {
    #         "name": "eddd",
    #         "age": 3
    #     }
    # ]
    # r = lambda s: s["name"]
    #
    # def fun(t):
    #     return t["name"]
    #
    # s = list(filter(fun, res))[0].get("name")
    # print(show[0].id)
    #
    # print(s)
    return render_template("index.html", page_data=page_data, comment_date=comment_date)


@blue.route("/add_post/")
def add_post():
    post = Post(
        title="我的第一篇文章",
        body="我第一次发文章有点激动，这是我的正文"
    )
    db.session.add(post)
    db.session.commit()
    return "ok"


@blue.route("/del_post/")
def del_post():
    return "ok"


@blue.route("/add_comment/")
def add_comment():
    comment = Comment(
        auther="老李",
        body="这是第二条评论，这文章好ａ",
        post_id=1,
    )
    db.session.add(comment)
    db.session.commit()
    return "ok"


@blue.route("/add_reply/")
def add_reply():
    comment = Comment(
        auther="老王",
        body="老李说的对",
        post_id=1,
        reply_id=3
    )
    db.session.add(comment)
    db.session.commit()
    return "ok"


@blue.route("/del_reply/")
def del_reply():
    return "ok"


@blue.route("/show_date/")
def show_data():
    post = Post.query.all()
    comment = Comment.query.filter_by(reply_id=None).all()
    reply = Comment.query.filter(not_(Comment.reply_id == None)).all()
    print("comment all", post[0].comments)
    print("id=3,reply",comment[2].replys)
    print(comment[0].replys)
    print(comment[2].replyd)
    print("post", post)
    print("reply all", reply)
    print("comment 不算回复的", comment)

    return "ok"
