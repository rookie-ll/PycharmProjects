from flask import Blueprint

app_blue = Blueprint('app_blue', __name__, template_folder='../../templates/adm')


def create_blue(app):
    app.register_blueprint(app_blue, url_prefix='/app_blue')


from . import views
