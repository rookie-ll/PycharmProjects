from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    textfeild = TextAreaField(
        validators=[
            DataRequired()
        ],
        render_kw={
            # "name": "editorContent",
            "lay - verify": "content",
            "id": "remarkEditor",
            "placeholder": "请输入内容",
            "class": "layui-textarea"
        }
    )

    submit = SubmitField(
        "提交留言",
        render_kw={
            "class": "layui-btn",
            "lay-submit": "formLeaveMessage",
            "lay - filter": "formLeaveMessage"
        }
    )


class ReplyForm(FlaskForm):
    reply = TextAreaField(
        validators=[
            DataRequired()
        ],
        render_kw={
            "lay - verify": "replyContent",
            "placeholder": "请输入回复内容",
            "class": "layui-textarea",
            "style": "min-height:80px;"
        }
    )
    submit = SubmitField(
        "回复",
        render_kw={
            "class": "layui-btn layui-btn-xs",
            "lay-submit": "formReply",
            "lay-filter": "formReply"
        }
    )
