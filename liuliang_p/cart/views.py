from . import app_cart
from flask import render_template
#注册蓝图路由
@app_cart.route('/cart')
def cart():
    return render_template('cart.html')