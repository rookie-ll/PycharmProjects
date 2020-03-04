from flask import Flask
from APP.views import blue
from flask_script import Manager
from APP.models import init_db
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(blueprint=blue)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sqlite3.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db=SQLAlchemy(app)
init_db(app)
manager=Manager(app=app)

@app.route('/')
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    manager.run()
