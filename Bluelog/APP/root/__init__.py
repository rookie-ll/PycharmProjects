from flask import Blueprint

adm = Blueprint('adm', __name__)


def create_blue(app):
    app.register_blueprint(adm, url_prefix='/adm')


from . import views
