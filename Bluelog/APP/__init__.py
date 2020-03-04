from flask import Flask
from APP.configs import Configing
from APP.ext import create_ext
from APP.root import create_blue as create_admin
from APP.blog import create_blue as create_home
#from .faker_views import insert_datas
#from APP import models


def create_app():
    app = Flask(__name__)

    #初始化配置

    app.config.from_object(Configing)

    # 初始化第三方插件
    create_ext(app)


    #初始化蓝图
    create_admin(app)
    create_home(app)




    return app
