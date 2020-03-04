import uuid

from flask import render_template, request, abort, redirect, url_for, flash
from webapp.forms import RegisterForm, LoginForm
from webapp.extends import db
from webapp.models import User
from . import user
from flask_login import login_user, logout_user, current_user, login_required


@user.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("b_index.index"))
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        print(name)
        u = User.query.filter_by(username=str(form.username.data)).first()
        print(u)
        if u is None:
            flash("用户名错误", "err")
        elif u.check_password(form.password.data):
            login_user(u)
            # if not next_is_valid(n):
            #     return abort(400)

            return redirect(request.args.get("next") or url_for("b_index.index"))
        else:
            flash("密码错误", "err")

    return render_template("login.html", form=form)


@user.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            emial=form.email.data,
            phone=form.phone.data,
            uuid=uuid.uuid4().hex,
            is_admin=False,
        )
        db.session.add(user)
        db.session.commit()
    return render_template("register.html", form=form)


@user.route("logout/")
@login_required
def logout():
    logout_user()
    return redirect(request.args.get("next") or url_for("b_index.index"))
