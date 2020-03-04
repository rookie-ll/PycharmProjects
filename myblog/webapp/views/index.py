from flask import render_template
from . import b_index



@b_index.route('/')
def index():
    return render_template("index.html")