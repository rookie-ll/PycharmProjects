from flask import Flask,Blueprint,current_app,render_template
import logging

blue=Blueprint("f_blue",__name__,template_folder='../templates')

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/index/')
def index():
    #current_app.logger.error()
    logging.error("hellob error")
    logging.warn("hello warn")
    logging.info("hello info")
    logging.debug("hello debug")
    return render_template('index.html')