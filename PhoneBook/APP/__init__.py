from flask import Flask,Blueprint
from APP.settings import Configs
from APP.views import create_blue
from APP.ext import init_etx


def create_app():
    app=Flask(__name__)

    #加载配置
    app.config.from_object(Configs)

    #加载第三方插件
    init_etx(app)

    # 注册蓝图
    create_blue(app)

    return app