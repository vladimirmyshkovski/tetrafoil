# coding: utf-8
import os
import glob2
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import create_app
from application.models import db
import sqlalchemy_utils
from application.models import Role, User
from application.utils.security import user_datastore
from flask_security import utils
from application.utils.socketio import socketio
import datetime

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)

# db migrate commands
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def create_user():
    with app.app_context():
        print('Committing to database ...')
        db.create_all()
        user_datastore.find_or_create_role(name='superadmin', description='Superadministrator')
        encrypted_password = utils.encrypt_password('iddqd3133122')
        db.session.commit()
        user_datastore.create_user(email='narnikgamarnikus@gmail.com', password=encrypted_password, confirmed_at=datetime.datetime.now())
        db.session.commit()
        user_datastore.add_role_to_user('narnikgamarnikus@gmail.com', 'superadmin')
        db.session.commit()
    print('SuperUser was created!')


@manager.command
def create_all():
    with app.app_context():
        print('Creating all ...')
        db.create_all()
    print('All is created!!')

@manager.command
def run():
    """Run app."""
    socketio.run(app, port=PORT)


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
