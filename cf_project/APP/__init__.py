from flask import Flask
from APP.ext import init_ext
from APP.settings import Configs, envs
from APP.views import init_blue


def create_app():
    app = Flask(__name__)
    #初始化配置
    app.config.from_object(envs.get('develoop'))
    # 注册蓝图
    init_blue(app)

    #初始化第三方插件
    init_ext(app)
    return app




