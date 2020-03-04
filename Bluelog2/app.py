from flask import Flask
from settings import Configing
app = Flask(__name__)
app.config.from_object(Configing)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
