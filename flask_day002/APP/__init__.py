from flask import Flask

from APP.settings import envs
from APP.ext import init_ext
from APP.views import init_blue
from APP.models import Student_jsj,Class_one


def create_app():
    app=Flask(__name__)
    #初始化配置
    app.config.from_object(envs.get("config"))
    #初始化第三方插件
    init_ext(app)
    #注册蓝图
    init_blue(app)

    return app