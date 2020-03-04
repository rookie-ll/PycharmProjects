from flask import Blueprint
#创建一个蓝图对象
app_cart=Blueprint('app_cart',__name__,template_folder='templates',static_folder='static')

from .views import app_cart
