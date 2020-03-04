import click
from flask import Flask
from APP.ext import create_ext, db
from APP.settings import configs
from APP.app_blue import create_blue as create_admin
from APP.blog import create_blue as create_home
# from APP.app_blue.views import create_blue as create_admin

from APP import models


def create_app(config_name):
    app = Flask(__name__)

    # 初始化配置
    # 通过类初始化
    app.config.from_object(configs.get(config_name))
    # 调用初始化函数
    configs.get(config_name).init_app(app)

    # 初始化第三方插件
    create_ext(app)

    # 初始化蓝图
    create_admin(app)
    create_home(app)

    return app
