from flask import Flask, jsonify, abort, request, g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from wsgiref.simple_server import make_server

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "lskadjflg23lkjsdfj"


def generate_token():
    s = Serializer(app.config["SECRET_KEY"], expires_in=3600)
    return s.dumps({"username": "liuliang"})


def check_token(token):
    s = Serializer(app.config["SECRET_KEY"])
    try:
        data = s.loads(token)
    except:
        return False
    g.username=data.get("username")
    return True


@auth.verify_password
def verify_password(username, password):
    if username == "liuliang" and password == "123123":
        return True
    else:
        #若用户名密码认证失败，再次使用ｔｏｋｅｎ认证
        return check_token(username)


@app.route("/token/")
@auth.login_required
def token():
    return generate_token()


@auth.error_handler
def unauthorized():
    return jsonify({"err": "错误，没有认证"}), 403


@app.errorhandler(404)
def page_not_fount(e):
    return jsonify({"error": "page not found"}), 404


@app.errorhandler(400)
def request_bead(e):
    return jsonify({"error": "request bead"}), 400


class UserApi(Resource):
    # 资源保护认证
    # decorators = [auth.login_required]
    method_decorators = [auth.login_required]

    def get(self, id):
        return {"method": "GET"}

    def post(self, id):
        return {"method": "POST"}

    def put(self, id):
        return {"method": "PUT"}

    def delete(self, id):
        return {"method": "DELETE"}


class UserListApi(Resource):
    def get(self):
        return {"userlist": "get"}

    def post(self):
        return {"userlist": "post"}


api.add_resource(UserApi, "/user/<int:id>/", endpoint="user")
api.add_resource(UserListApi, "/user/", endpoint="users")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
