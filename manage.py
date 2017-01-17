# coding: utf-8
import os
import glob2
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from application import create_app
from application.models import db
import sqlalchemy_utils
from application.utils.socketio import socketio
from application.models import Role, User

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)

# db migrate commands
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def create_roles():
    manager = Role(name = 'manager')
    admin = Role(name = 'admin')
    superadmin = Role(name = 'superadmin')
    create_super_user = User(name='admin', email='admin@admin.admin', password='admin', role=3)
    with app.app_context():
        print('Committing to database ...')
        db.session.add(manager)
        db.session.add(admin)
        db.session.add(superadmin)
        db.session.add(create_super_user)
        db.session.commit()
    print('Added.')


@manager.command
def run():
    """Run app."""
    app.run(port=PORT)


@manager.command
def live():
    """Run livereload server"""
    from livereload import Server

    server = Server(app)

    map(server.watch, glob2.glob("application/pages/**/*.*"))  # pages
    map(server.watch, glob2.glob("application/macros/**/*.html"))  # macros
    map(server.watch, glob2.glob("application/static/**/*.*"))  # public assets

    server.serve(port=PORT)


@manager.command
def build():
    """Use FIS to compile assets."""
    os.system('gulp')
    os.chdir('application')
    os.system('fis release -d ../output -opmD')


if __name__ == "__main__":
    manager.run()
