from app.libs.readprint import Readprints

user = Readprints("user")


@user.route("/get")
def userindex():
    return "myuser index"
