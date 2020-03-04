from redis import StrictRedis

class Configs():
    # 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/classmd1'
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_RECORD_QUERIES=True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SECRET_KEY="ASLKDJFAGJ34234Jjskljlkjaslfjajgo2"

    #配置把session保存到redis
    SESSION_TYPE="redis"
    SESSION_USE_SIGNER=True
    SESSION_PERMANENT=True
    SESSION_REDIS=StrictRedis(host="127.0.0.1",port="6379",db=0)







envs={
    "config":Configs
}