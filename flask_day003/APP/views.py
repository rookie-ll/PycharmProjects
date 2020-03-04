from flask import Blueprint

blue=Blueprint("f_blue",__name__)
def init_blue(app):

    app.register_blueprint(blueprint=blue)


@blue.route('/index/')
def index():
    return 'hello'