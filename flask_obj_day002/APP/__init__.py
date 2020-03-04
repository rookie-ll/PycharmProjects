

from flask import Flask

from APP.ext import init_ext
from APP.views import init_blue


def create_app():
    app=Flask(__name__)

    #配置文件

    #安装插件

    init_ext(app)

    #安装视图
    init_blue(app)
