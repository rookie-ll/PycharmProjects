class Configs(object):
    DEBUG = True
    SECRET_KEY="LSKDJFlsakfjsldkfj232lfkj2flksdjf"
    #dialect + driver: // username: password @ host:port / database
    SQLALCHEMY_DATABASE_URI="mysql://root:123456@127.0.0.1:3306/phonebook"
    SQLALCHEMY_ECHO=True

dic=dict(
    configs=Configs
)
#type()
