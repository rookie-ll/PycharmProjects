import os

from flask_script import Manager
from APP import create_app
from flask_migrate import Migrate, MigrateCommand

from APP.ext import db

app = create_app(config_name=os.environ.get("FLASK_CONFIG") or "Development")

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.name)
    print(app.url_map)
    manager.run()
