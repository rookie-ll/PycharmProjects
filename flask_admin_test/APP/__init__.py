import click
from flask import Flask
from APP.settings import Config
from APP.extends import app_extend, db
from APP import models
from APP.views import app_blueprints


def create_app():
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(Config)

    # 初始化第三方插件
    app_extend(app)

    # 初始化蓝图对象
    app_blueprints(app)

    # @app.cli.command()
    # def forge():
    #     """Generate fake data."""
    #     from APP.fakers import add_class,add_student,add_teacher
    #
    #     # db.drop_all()
    #     # db.create_all()
    #
    #     #click.echo('Generating the administrator...')
    #     #add_class()
    #
    #     click.echo('Generating %d categories...')
    #     add_student()
    #
    #     click.echo('Generating %d posts...')
    #     add_teacher()
    #
    #     click.echo('Done.')
    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
    def forge(category, post, comment):
        """Generate fake data."""
        from APP.faskr_bluelog import fake_admin, fake_categories, fake_posts, fake_comments, fake_links

        db.drop_all()
        db.create_all()

        click.echo('Generating the administrator...')
        fake_admin()

        click.echo('Generating %d categories...' % category)
        fake_categories(category)

        click.echo('Generating %d posts...' % post)
        fake_posts(post)

        click.echo('Generating %d comments...' % comment)
        fake_comments(comment)

        click.echo('Generating links...')
        fake_links()

        click.echo('Done.')
    return app
