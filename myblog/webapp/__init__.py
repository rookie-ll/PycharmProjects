from flask import Flask
from .extends import app_extends
from .views import app_blue
from .configs import config
from .models import blog
from .libs import app_filter


def create_app():
    app = Flask(__name__)

    # 配置
    app.config.from_object(config.get("development"))

    # 第三方插件
    app_extends(app)

    # 蓝图
    app_blue(app)

    # 自定义过滤器
    app_filter(app)
    return app
