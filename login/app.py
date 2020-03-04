# -*- coding: utf-8 -*f

from flask import Flask, redirect, url_for,render_template
from flask_bootstrap import Bootstrap

from blue_app.views import blue
from flask_script import Manager
from blue_app.views2 import blue as blue2

app = Flask(__name__)
app.config['SECRET_KEY']="sldkfj23rrwfssdfsdf"
app.register_blueprint(blue,url_prefix="/login")
app.register_blueprint(blue2,url_prefix='/index')

manager=Manager(app=app)

bootstrap=Bootstrap(app=app)

@app.route('/')
def hello_world():
    return render_template('main.html')


if __name__ == '__main__':
    manager.run()
