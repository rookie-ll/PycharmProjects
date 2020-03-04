# -*- coding: utf-8 -*f
from blue_app import blue
from flask import render_template, request, Response, redirect, url_for,session


@blue.route("/home/")
def home():
    #username=request.cookies.get('user')
    username=session.get('user')
    return render_template('home.html',username=username)


@blue.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username=request.form.get('username')
        ret=Response(response="登录成功:%s" %username)
        #ret.set_cookie("user",username)
        session['user']=username
        print(username)
        return ret

@blue.route('/exit/')
def exit():
    delt=redirect(url_for('frst_blue.home'))
    #delt.delete_cookie('user')
    return delt