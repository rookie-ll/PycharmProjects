from flask import Blueprint

blog = Blueprint('blog', __name__)


def create_blue(app):
    app.register_blueprint(blog, url_prefix='/blog')


from . import views
