from flask import Blueprint

b_index = Blueprint("b_index", __name__, static_folder="../static", template_folder="../templates")
blog = Blueprint("blog", __name__, static_folder="../static", template_folder="../templates")
blog_read = Blueprint("blog_read", __name__, static_folder="../static", template_folder="../templates")
comment = Blueprint("comment", __name__, static_folder="../static", template_folder="../templates")
link = Blueprint("link", __name__, static_folder="../static", template_folder="../templates")
diary = Blueprint("diary", __name__, static_folder="../static", template_folder="../templates")
user = Blueprint("user", __name__, static_folder="../static", template_folder="../templates")


def app_blue(app):
    app.register_blueprint(b_index)
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(blog_read, url_prefix="/read")
    app.register_blueprint(comment, url_prefix="/comment")
    app.register_blueprint(link, url_prefix="/link")
    app.register_blueprint(diary, url_prefix="/diary")
    app.register_blueprint(user,url_prefix="/user")


from . import index
from . import blog_view
from . import read_view
from . import comment_view
from . import link_view
from . import diary_view
from . import user_views
