
from flask import Flask

from APP.ext import init_ext
from APP.views import init_blue


def create_app():
    app=Flask(__name__)

    #初始化配置文件

    #初始化蓝图
    init_blue(app)
    #初始化第三方
    init_ext(app)
    return app