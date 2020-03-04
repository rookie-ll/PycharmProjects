from flask import Blueprint

app_goods=Blueprint('app_goods',__name__)

@app_goods.route('/goods',)
def goods():
    return "hello goos"