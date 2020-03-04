class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/Bluelog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY='slkfjSLDKFJ23R2LKSFDJF4sldkfj3232flskdfj'
    BABEL_DEFAULT_LOCALE = 'zh_CN'
