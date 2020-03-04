from flask import Blueprint

blog = Blueprint('blog', __name__)


def create_blue(app):
    app.register_blueprint(blog)


from . import views
