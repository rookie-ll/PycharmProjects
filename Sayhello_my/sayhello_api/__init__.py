from flask import Flask, render_template
from sayhello_api import ext
from sayhello_api import settings
from sayhello_api import models


def create_app():
    app = Flask(__name__)

    # 初始化配置

    app.config.from_object(settings.config_list.get("debuger"))

    # 初始化第三方插件

    ext.insert_ext(app)

    # 注册蓝图
    from sayhello_api import views
    views.create_blueprint(app)

    # 错误页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("errors/500.html"), 500

    return app
