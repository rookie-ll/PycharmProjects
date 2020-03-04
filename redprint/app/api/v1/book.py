from app.libs.readprint import Readprints

book = Readprints("book")


@book.route("/create")
def book_index():
    return "mybook index"
