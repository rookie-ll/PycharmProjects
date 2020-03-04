class Configing(object):
    DEBUG = True

    # mysql: // scott: tiger @ localhost / mydatabase
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/Bluelog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "slkdfjSDFK32LJL23kldsjf"
