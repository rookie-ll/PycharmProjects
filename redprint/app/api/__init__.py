from .v1 import create_blueprint


def app_blue(app):
    app.register_blueprint(create_blueprint(), url_prefix="/v1")
