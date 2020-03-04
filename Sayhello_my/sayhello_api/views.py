from flask import Blueprint, render_template, request, flash, redirect, url_for
from faker import Faker
from sayhello_api.models import db, Message

api = Blueprint("api", __name__, template_folder="../templates", static_folder="../static")


def create_blueprint(app):
    app.register_blueprint(api)


@api.route("/<int:page>/", methods=["GET", "POST"])
def index(page=None):
    if page == None:
        page = 1
    print(page)
    page_data = Message.query.order_by(Message.timestamp.desc()).paginate(page, per_page=2)
    print(page_data)
    if request.method == "GET":
        return render_template("index.html", page_data=page_data, page=1)
    if request.method == "POST":
        name = request.form.get("name")
        msg = request.form.get("msg")
        if len(name) <= 20 and len(msg) <= 200:
            message = Message(
                name=name,
                body=msg,
            )
            db.session.add(message)
            db.session.commit()
            flash("成功", "ok")
            return redirect(url_for("api.index", page=1))
        else:
            flash("失败", "err")

    return render_template("index.html", page_data=page_data, page=1)


@api.route("/create_data")
def create_data():
    fake = Faker()

    for i in range(10):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )

        db.session.add(message)

    db.session.commit()
    return "data　create "
