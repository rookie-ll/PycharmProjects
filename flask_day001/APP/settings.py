def get_db_uel(dbinfo):
    ENGINE=dbinfo.get('ENGINE') or 'mysql'
    DRIVER=dbinfo.get('DRIVER') or 'pymysql'
    USER=dbinfo.get('USER') or 'root'
    PASSWORD=dbinfo.get('PASSWORD') or 'root'
    HOST=dbinfo.get('HOST') or 'localhost'
    PORT=dbinfo.get('PORT') or '3306'
    NAME=dbinfo.get('NAME') or 'class_mdzz'
    return  "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)

class Configs:
    DEBUG=False
    TESTING=False
    SECRET_KEY="fsflf23AFAFf332wefwefwf"
    #SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DeveloopConfig(Configs):
    DEBUG=True
    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
        'NAME':'classmd'
    }
    SQLALCHEMY_DATABASE_URI=get_db_uel(DATABASE)



class TestingConfig(Configs):
    TESTing=True

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
        'NAME':'sqldbname'
    }
    SQLALCHEMY_DATABASE_URI=get_db_uel(DATABASE)


class StagingConfig(Configs):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'sqldbname'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uel(DATABASE)


class ProuductConfig(Configs):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'sqldbname'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uel(DATABASE)


envs={
    'develoop':DeveloopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'prouduct':ProuductConfig
}