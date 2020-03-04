from flask import render_template
from . import link


@link.route("/")
def link_index():
    return render_template("link.html")