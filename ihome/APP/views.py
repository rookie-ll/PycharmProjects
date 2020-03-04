from flask import Flask,Blueprint,current_app,render_template

static_blue=Blueprint("static_blue",__name__,template_folder="../templates")


def init_staticblue(app):
    app.register_blueprint(blueprint=static_blue)


@static_blue.route("/<re(r'.*'):static_file_name>")
def static_fun(static_file_name):
    if not static_file_name:
        static_file_name="index.html"
    if static_file_name!="favicon.ico":
        static_file_name="html/"+static_file_name

    return current_app.send_static_file(static_file_name)

''''@static_blue.route('/index/')
def index():
    return render_template('index.html')
'''