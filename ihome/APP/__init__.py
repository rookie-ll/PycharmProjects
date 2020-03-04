from flask import Flask

from APP.views import init_staticblue
from utils.commons import ReBaseconverter
from APP.settings import Configs
from APP.ext import create_ext
from APP import models


def create_app():
    app = Flask(__name__)
    # 初始化配置文件
    app.config.from_object(Configs)
    # 初始化插件
    create_ext(app)
    # 初始化自定义函数
    app.url_map.converters["re"] = ReBaseconverter

    # 初始化蓝图
    init_staticblue(app)
    return app
