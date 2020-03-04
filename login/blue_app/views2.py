from blue_app import blue
from flask import render_template, url_for, redirect, request, flash


@blue.route('/index/')
def deffff():
    return render_template('set.html')

@blue.route('/main')
def mainn():
    return render_template('main.html')


@blue.route('/helloboot')
def bootst():
    return render_template('hello_bookstrap.html')


@blue.route('/userlogin/',methods=['GET','POST'])
def user_login():
    if request.method=='GET':
        return render_template('user_login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        flash('hello')
        return render_template('say_hello.html')