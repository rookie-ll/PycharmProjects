from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField(
        "搜索",
        validators=[
            DataRequired()
        ],
        render_kw={
            "id": "searchtxt",
            "placeholder": "输入关键字搜索"
        }
    )
    submit = SubmitField(
        "",
        render_kw={
            "class": "fa fa-search",
            "style": "background: none"
        }
    )



