from flask import Blueprint

#1创建一个蓝图对象，蓝图就是一个小模块的抽象概念

app_order=Blueprint("app_order",__name__)

#２注册蓝图路由
@app_order.route('/order')
def order():
    return 'this is a order'