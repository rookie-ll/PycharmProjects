from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet('photos', IMAGES)
login_manager = LoginManager()


def app_extends(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 上传文件配置
    configure_uploads(app, photos)
    patch_request_class(app, size=None)

    login_manager.login_view = "user.login"
    login_manager.login_message = "需要登陆才能访问"
    # 用户保护级别
    # None 不开启
    # basic 默认
    # strong 开启
    login_manager.session_protection = 'strong'
