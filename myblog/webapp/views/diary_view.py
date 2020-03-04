from flask import render_template
from . import diary


@diary.route("/")
def diary_index():
    return render_template("diary.html")
