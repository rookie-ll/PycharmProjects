from flask import Flask, render_template, request, url_for, make_response, json, redirect, Response
from pymysql import connect
from flask_script import Manager

#from goods import goods
from order import app_order
from cart import app_cart
from goods import app_goods

app = Flask(__name__)
#app.route('/goods')(goods)

#3注册蓝图
app.register_blueprint(app_order,url_prefix='/orders')
app.register_blueprint(app_cart,url_prefix='/carts')
app.register_blueprint(app_goods,url_prefix='/goods')

manger=Manager(app)
#链接数据库
def conn():
    # pymysql链接数据库
    # con = connect(host='127.0.0.1', port='3306', user='root', password='123456', database='lianxi', charset='utf8')
    # 获取游标
    con = connect(host='localhost', port=3306, database='stock_db', user='root', password='123456', charset='utf8')
    cursor = con.cursor()
    sql = '''select * from info;'''
    cursor.execute(sql)
    con.commit()
    a = cursor.fetchall()
    # s=str(a)
    # 关闭游标和链接
    cursor.close()
    con.close()
    return a

@app.route('/index',methods=['GET','POST'])
def hello_world():
    print(app.url_map)
    s=conn()
    req=request.args.get("name")
    valu=request.values.get("name")
    age=request.args.get('age')
    datas=request.data
    print(datas)
    return "name=%s,age=%s,datas=%s"%(req,age,datas)

@app.route('/redes')
def hello():
    response=make_response("<h2>羞羞哒</h2>")
    response.headers["Content-Type"]="text/html; charset=utf-8"
    return response,404

@app.route('/hello',methods=['GET,POST'])
def index():
    wode=request.data
    wode2=request.form.get('username')
    wode3=request.form.get('password')
    return render_template("index.html",wode2=wode2,wode3=wode3)

@app.route('/getuuid<uuid:an>/',methods=['GET','POST'])
def get_uuid(an):
    return an


@app.route('/gett')
def get():
    return render_template('index2.html')


@app.route('/reps')
def reqss():
    ret=render_template('index2.html')
    print(ret)
    print(type(ret))
    response=make_response("<h1>ｍｄｚｚ</h1>")
    print(response)
    print(type(response))

    return response


@app.route("/redir")
def red():
    rest=redirect(url_for("reqss"))
    print(rest)
    print(type(rest))
    return rest

@app.route("/json/")
def json_666():
    #sest = json.jsonify({'name': 'value'})
    sest=json.jsonify(name="刘亮",age=19)
    print(sest)
    print(type(sest))
    return sest


@app.route('/login',methods=['GET','POST'])
def login():
    name=request.form.get("name")
    password=request.form.get("password")
    print(name)
    print(password)
    if name=="123" and password=="321":
        print("登录成功")
    else:
        print("ｍｄｚｚ")
    return render_template("login.html")



@app.route('/request',methods=['GET','POST'])
def requests():
    print(type(request))
    req=request.data
    print(req)
    return "请求"

"""
    print(a)
    html='''
        <ul>
        <li>%s</li>
        <li>%s</li>
        <li>%s</li>
        <ul>
    '''
    htm=''
    for i in a:
        htm += html%(i[0],i[1],i[2])
        print(i[0])

    return htm
    """
if __name__ == '__main__':
    manger.run()
