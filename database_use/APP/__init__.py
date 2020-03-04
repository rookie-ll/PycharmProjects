from flask import Flask
from APP.ext import create_ext
from APP.setting import config_list
from APP.views import create_blue
import APP.module
import APP.module2


def create_app():
    app = Flask(__name__)

    app.config.from_object(config_list.get("debugs"))

    create_ext(app)

    create_blue(app)
    return app
