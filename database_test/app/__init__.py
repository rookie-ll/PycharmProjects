from flask import Flask

from .views import init_blue
from .moels import init_ext
from .setting import Configs


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configs)
    init_ext(app)
    init_blue(app)
    return app
