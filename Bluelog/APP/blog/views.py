from APP.blog import blog
from flask import render_template, url_for,redirect


@blog.route('/')
def index():
    return render_template('blog/index.html')

@blog.route('/about/')
def about():

    return redirect(url_for('sidebar',_external=True))

@blog.route('/sidebar/')
def sidebar():
    return render_template('blog/_sidebar.html')

