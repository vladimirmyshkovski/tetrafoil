# coding: utf-8
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ._base import db
from .base import Base
from sqlalchemy.orm import relationship
from flask_socketio import emit
from flask import g, url_for
from .notification import Notification
import humanize


class User(Base, db.Model):
    
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    avatar = db.Column(db.String(200), default='default.png')
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    organisations = db.relationship('Organisation', backref="user")
    projects = db.relationship('Project', backref="user")
    contacts = db.relationship('Contact', backref="user")
    activities = db.relationship('Activity', backref="user")        
    
    @staticmethod
    def get_unread_notifs(self, reverse=False):
        """Get unread notifications with titles, humanized receiving time
        and Mark-as-read links.
        """
        notifs = []
        unread_notifs = Notification.query.filter_by(created_by=self.id, has_read=False)
        for notif in unread_notifs:
            notifs.append({
                'title': notif.title,
                'received_at': humanize.naturaltime(datetime.now() - notif.received_at),
                'mark_read': url_for('crm.view', keyword=Notification)
            })

        if reverse:
            return list(reversed(notifs))
        else:
            return notifs

    @staticmethod
    def create_notification(self, action, title, message):
        """
        Create a User Notification
        :param user: User object to send the notification to
        :param action: Action being performed
        :param title: The message title
        :param message: Message
        """
        saved = Notification.create(created_by=self.id,
                                    has_read=False,
                                    action=action,
                                    title=title,
                                    message=message,
                                    received_at=datetime.now())
        if saved:
            User.push_user_notification(self)
    

    @staticmethod
    def push_user_notification(self):
        """
        Push user notification to user socket connection.
        """
        user_room = 'user_{}'.format(self.id)
        emit('notification',
             {'meta': 'New notifications',
              'notifs': self.get_unread_notifs(self)},
             room=user_room,
             namespace='/notifs')
        print('notification was pushed!')
    

    def __setattr__(self, name, value):
        # Hash password when set it.
        if name == 'password':
            value = generate_password_hash(value)
        super(User, self).__setattr__(name, value)


    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %s>' % self.name
