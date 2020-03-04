from flask import Blueprint,Flask

blue=Blueprint("b_first",__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/index/')
def index():
    return "ojbk"