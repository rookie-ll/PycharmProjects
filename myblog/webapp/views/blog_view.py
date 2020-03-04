from flask import render_template, request
from webapp.models import Post, Category, Comment
from webapp.forms import SearchForm
from . import blog


@blog.route("/", methods=["GET", "POST"])
def blog_index():
    form = SearchForm()
    categories = Category.query.all()
    page = request.args.get("page", 1, type=int)
    id = request.args.get("id", type=int)
    if id:
        page_date = Post.query.filter(
            Post.category_id == id
        ).order_by(Post.timestamp.desc()).paginate(page=page, per_page=10)
    else:
        page_date = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=10)

    if form.validate_on_submit():
        key = form.data.get("search")
        page_date = Post.query.filter(
            Post.title.ilike("%" + key + "%")
        ).order_by(
            Post.timestamp.desc()
        ).paginate(page=page, per_page=10)

    return render_template("article.html", form=form, page_date=page_date, cate=categories)


@blog.route("/")
def host_post():
    pass
