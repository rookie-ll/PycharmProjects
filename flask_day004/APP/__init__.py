from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

from APP.ext import init_ext
from APP.views import init_blue


def create_app():
    app=Flask(__name__)

    init_blue(app)

    init_ext(app)

    return app

#设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)
#设置日志记录器，指明日志保存路径,每个日志的文件大小，保存文件的数量上限
file_log_header=RotatingFileHandler("logs/log",maxBytes=222,backupCount=10)
#设置日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#为刚创建的日志记器设置日志格式
file_log_header.setFormatter(formatter)
#为全局日志工具对象（ｆｌａｓｋ　ａｐｐ使用的）添加日志记录器
logging.getLogger().addHandler(file_log_header)