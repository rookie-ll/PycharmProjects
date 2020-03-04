from flask import Blueprint
from app.api.v1.book import book
from app.api.v1.user import user


def create_blueprint():
    v1 = Blueprint("v1", __name__)
    book.register(v1, url_prefix="/book")
    user.register(v1, url_prefix="/user")
    return v1
