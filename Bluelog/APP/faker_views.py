import random

from flask import Blueprint
from sqlalchemy.exc import IntegrityError

from APP.me_models import db, Admin, Category, Post, Comment
from faker import Faker

fakers_blue = Blueprint('fakers_blue', __name__)


def insert_datas(app):
    app.register_blueprint(fakers_blue, url_prefix='/insert_data')


@fakers_blue.route('/add_admin/')
def insert_data():
    admin = Admin(
        username='root',
        password_hash="helloflask",
        blog_title='Bluelog',
        blog_sub_title="No, I'm the real thing.",
        name='liuliang',
        about="slkjflsjflslf",
    )
    db.session.add(admin)
    db.session.commit()
    return "add root is ok"


@fakers_blue.route('/add_catcgories/<int:count>/')
def insert_data2(count=10):
    fake = Faker()
    category = Category(name="Default")
    db.session.add(category)
    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
    return "add user is ok"


@fakers_blue.route('/add_post/<int:count>/')
def insert_data3(count=50):
    fake = Faker()
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            add_time=fake.date_time_this_year(),
            category=Category.query.get(random.randint(1, Category.query.count()))
        )
        db.session.add(post)
    db.session.commit()
    return "add user is ok"


@fakers_blue.route('/add_comments/<int:count>/')
def insert_data4(count=500):
    fake = Faker()
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            add_time=fake.date_time_this_year(),
            reviewed=True,
            postr=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    salt = int(count * 0.1)
    for i in range(salt):
        # 未审核评论
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            add_time=fake.date_time_this_year(),
            reviewed=False,
            postr=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    comment = Comment(
        author='Mima Kirigoe',
        email='mima@example.com',
        site='example.com',
        body=fake.sentence(),
        add_time=fake.date_time_this_year(),
        from_admin=True,
        reviewed=True,
        postr=Post.query.get(random.randint(1, Post.query.count()))
    )
    db.session.add(comment)
    db.session.commit()
    # 回复
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            add_time=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            postr=Post.query.get(random.randint(1, Post.query.count())))
        db.session.add(comment)
    db.session.commit()
    return "add user is ok"


@fakers_blue.route('/add_post/<int:count>/')
def insert_data5(count=10):
    fake = Faker()
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            add_time=fake.date_time_this_year(),
            category=Category.query.get(random.randint(1, Category.query.cout()))
        )
    return "add user is ok"
