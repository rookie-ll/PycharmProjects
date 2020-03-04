class Configs(object):
    # mysql://scott:tiger@localhost/mydatabase
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/test3"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Configs_2(Configs):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/Bluelog"

config_list = dict(
    debugs=Configs
)
