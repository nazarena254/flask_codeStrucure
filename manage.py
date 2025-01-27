from flask import Flask
from app import create_app
from flask_script import Manager,Server
# from  flask_migrate import Migrate, MigrateCommand

# from app.models import User


# Creating app instance
app = create_app('development')   # during development
#app = create_app('production')  # during production/deployment to heroku stage
# app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)

# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)


# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()
