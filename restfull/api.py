from flask import Flask, jsonify, abort, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["DEBUG"] = True
posts = [
    {
        "id": 1,
        "name": "老王",
        "age": 18,
        "content": "python真特码好学"
    },
    {
        "id": 2,
        "name": "老李",
        "age": 18,
        "content": "python真特嘛难学"
    }
]


@auth.verify_password
def verify_password(username, password):
    if username == "liuliang" and password == "123123":
        return True
    else:
        return False


@auth.error_handler
def unauthorized():
    return jsonify({"err": "错误，没有认证"}), 403


@app.errorhandler(404)
def page_not_fount(e):
    return jsonify({"error": "page not found"}), 404


@app.errorhandler(400)
def request_bead(e):
    return jsonify({"error": "request bead"}), 400


@app.route('/posts', methods=['GET'])
@auth.login_required
def posts_list():
    # return "GET:博客列表"
    return jsonify({"posts": posts})


@app.route('/posts/<int:pid>/', methods=['GET'])
def post(pid):
    # return "GET:第%s条博客" % pid
    p = list(filter(lambda f: f['id'] == pid, posts))
    if len(p):
        abort(404)
    return jsonify(p[0])


@app.route('/posts', methods=['POST'])
def new_posts():
    # return "POST:新增博客成功"
    if not request.json or "name" not in request.json or "age" not in request.json or "content" not in request.json:
        abort(400)
    if posts:
        p = {
            "id": posts[-1]["id"] + 1,
            "age": request.json['age'],
            "name": request.json['name'],
            "content": request.json['content']
        }
    else:
        p = {
            "id": 1,
            "age": request.json['age'],
            "name": request.json['name'],
            "content": request.json['content']
        }
    posts.append(p)

    return jsonify({"posts": p}), 201


@app.route('/posts/<int:pid>/', methods=['PUT'])
def up_posts(pid):
    # return "PUT:%s修改博客成功" % pid
    if pid:
        p = list(filter(lambda t: t["id"] == pid, posts))
        if len(p) == 0:
            abort(400)
        p[0]["age"] = request.json.get("age", p[0]["age"])
        p[0]["name"] = request.json.get("name", p[0]["name"])
        p[0]["content"] = request.json.get("content", p[0]["content"])
        if "age" in request.json:
            pass
        if "name" in request.json:
            pass
        if "content" in request.json:
            pass

    return jsonify({"posts": posts})


@app.route('/posts/<int:pid>/', methods=['DELETE'])
def del_posts(pid):
    # return "PUT:%s删除博客成功" % pid
    if pid:
        p = list(filter(lambda t: t["id"] == pid, posts))
        if len(p):
            posts.remove(p[0])
        else:
            abort(404)
    #
    # if pid:
    #     for i in posts:
    #         if i["id"] == pid:
    #             posts.remove(i)
    #         else:
    #             abort(404)
    return jsonify({"posts": posts}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
