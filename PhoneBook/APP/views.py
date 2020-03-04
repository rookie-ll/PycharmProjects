from _operator import or_

from flask import Blueprint, Flask, render_template, redirect, url_for, request, flash
from APP.models import db, Class

blue = Blueprint("blue", __name__, template_folder="../templates")


def create_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route("/")
def index():
    m_class = Class.query.all()
    return render_template("index.html", m_class=m_class)


@blue.route("/add_class/", methods=["GET", "POST"])
def add_class():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == "POST":
        if request.form.get("s_name") and request.form.get("phone") and len(request.form.get("phone")) == 11:
            name_sum = Class.query.filter(request.form.get("s_name") == Class.store_name).count()
            phone_sum = Class.query.filter(request.form.get("phone") == Class.phone).count()
            if name_sum == 1 or phone_sum == 1:
                flash("店铺名已经存在", "err")

            else:
                print(type(request.form))
                print(request.form)
                class_add = Class(
                    store_name=request.form.get("s_name"),
                    phone=request.form.get("phone"),
                    phone2=request.form.get("phone2"),
                    rem=request.form.get("rem")
                )
                db.session.add(class_add)
                db.session.commit()
                flash("添加成功", "ok")
        else:
            flash("店铺名称不能为空，且必须填写一个电话号码", "err")
    return redirect(url_for("blue.index"))


@blue.route("/del_class/<int:id>/", methods=["GET", "POST"])
def del_class(id=None):
    if id == None:
        raise 404
    d_class = Class.query.filter_by(id=id).first_or_404()
    db.session.delete(d_class)
    db.session.commit()
    print(d_class)
    flash("删除成功", "ok")
    return redirect(url_for("blue.index"))


@blue.route("/up_class/<int:id>/", methods=["GET", "POST"])
def up_class(id=None):
    e_class = Class.query.filter_by(id=id).first_or_404()
    if request.method == "GET":
        return render_template("edit.html", e_class=e_class)
    if request.method == "POST":
        if id == None:
            raise 404

        if request.form.get("s_name") and request.form.get("phone"):
            name_sum = Class.query.filter(request.form.get("s_name") == Class.store_name).count()
            phone_sum = Class.query.filter(request.form.get("phone") == Class.phone).count()
            # if name_sum == 1 or phone_sum == 1:
            # flash("店铺名已经存在", "err")

            # else:
            print(type(request.form))
            print(request.form)

            e_class.store_name = request.form.get("s_name"),
            e_class.phone = request.form.get("phone"),
            e_class.phone2 = request.form.get("phone2"),
            e_class.rem = request.form.get("rem")

            db.session.add(e_class)
            db.session.commit()
            flash("添加成功", "ok")
            return redirect(url_for("blue.index"))
        else:
            flash("店铺名称不能为空，且必须填写一个电话号码", "err")
    return render_template("edit.html", e_class=e_class)


@blue.route("/show_class/<int:page>/")
def show_class(page=None):
    if page==None:
        page=1
    key = request.args.get("key", "")
    s_class = Class.query.filter(
        or_(Class.store_name.like("%" + key + "%"),Class.phone.like("%" + key + "%"))
    ).paginate(page, per_page=2)
    return render_template("search.html", s_class=s_class)
