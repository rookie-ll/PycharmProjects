from flask import Flask

from APP import settings
from APP.etx import init_etx
from APP.settings import envs
from APP.views import create_blue
from APP.models import Student,Hello

def create_app():
    app=Flask(__name__,template_folder='../templates')


    #初始化配置
    app.config.from_object(envs.get('develoop'))

    #注册蓝图
    create_blue(app)

    # 初始化第三方插件
    init_etx(app)


    return app
