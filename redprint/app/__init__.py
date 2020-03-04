from flask import Flask
from app.api import app_blue


def create_app():
    app = Flask(__name__)
    app.debug = True
    app_blue(app)
    return app
