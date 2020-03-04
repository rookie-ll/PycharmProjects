import os


class Configs():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/sayhello"
    DEBUG = True
    #BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    DEBUG_TB_INTERCEPT_REDIRECTS=False

config_list = dict(
    debuger=Configs
)
