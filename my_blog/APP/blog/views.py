from APP.blog import blog
from flask import url_for, render_template, redirect


@blog.route('/')
def index():
    return render_template('blog/index.html')


@blog.route('/about/')
def about():
    return render_template('blog/about.html')


@blog.route('/contact/')
def contact():
    return render_template('blog/contact.html')


@blog.route('/single/')
def single():
    return render_template('blog/single.html')
