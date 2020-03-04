from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)

#配置链接数据库
class Config_app(object):
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/book_project'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_ECHO=True
    SECRET_KEY="SDFSADFASsdfsdfagafasdf"

app.config.from_object(Config_app)
db=SQLAlchemy(app)

#创建flask脚本管理工具对象
manager=Manager(app)

#创建数据库迁移工具对象
#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate=Migrate(app,db)

#向manager对象中添加数据库的操作命令
#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

#定义模型类
class Book_info(db.Model):
    """书名"""
    __tablename__='tab_book'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    author_id=db.Column(db.Integer,db.ForeignKey("tab_author.id"))


class Author(db.Model):
    """作者"""
    __tablename__="tab_author"
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    books=db.relationship("Book_info",backref="author")
    email=db.Column(db.String(64))

#创建表单模型类
class AuthorBookfrom(FlaskForm):
    author_name=StringField(label="作者",validators=[DataRequired("作者必填")])
    book_name=StringField(label="书籍",validators=[DataRequired("书籍必填")])
    submit=SubmitField(label="提交")

@app.route('/',methods=['GET','POST'])
def hello_world():
    #构建表单
    form=AuthorBookfrom()
    if form.validate_on_submit():
        #验证表单成功，提取表单数据
        author_name=form.author_name.data
        book_name=form.book_name.data
        #保存数据库
        author=Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        #book=Book_info(name=book_name,author=author.id)
        book=Book_info(name=book_name,author=author)
        db.session.add(book)
        db.session.commit()

    #查询数据库
    author_li=Author.query.all()
    return render_template("author.html",authors=author_li,form=form)


# @app.route('/delete_book',methods=['POST'])
# def delete_book():
#     ret=request.get_json()
#     book_id=ret.get("book_id")
#
#     #删除数据
#     book=Book_info.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     #"Content-Type":"application/json"
#     return jsonify(code=0,message="OK")

#/delete_book?book_id=xx
@app.route('/delete_book',methods=['GET'])
def delete_book():
    book_id=request.args.get("book_id")

    #删除数据
    book=Book_info.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    '''
    db.drop_all()
    db.create_all()


    a1=Author(name="刘亮")
    a2=Author(name="爱吃萝卜的猪")
    a3=Author(name="爱吃青菜的猫")
    db.session.add_all([a1,a2,a3])
    db.session.commit()

    b1=Book_info(name="不知道啥书",author_id=a1.id)
    b2=Book_info(name="都市奇缘",author_id=a2.id)
    b3=Book_info(name="我的小可爱",author_id=a3.id)
    db.session.add_all([b1,b2,b3])
    db.session.commit()
'''
    #app.run()
    manager.run()

#创建迁移仓库
#python app;py db init
#创建迁移脚本
#python app.py db migrate
#更新数据库
#python app.py db upgrade
#版本记录
#python app.py db history
#回退版本
#python app.py db downgrade 版本号
