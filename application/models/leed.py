# coding: utf-8
from datetime import datetime
from .base import *
from ..utils.socketio import push_notification_to_all_users
from ..models import Notification

class Leed(Base):
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), unique=True)

    '''
    @staticmethod
    def push_notification():
    	title = 'New leed was created!'
    	message = 'Take leed, until you took another'
    	push_notification_to_all_users(title, message)

    @staticmethod
    def create_notification():
    	title = 'New leed was created!'
    	message = 'Take leed, until you took another'
    	saved = Notification.create(
    		created_by=1,
    		has_read=False,
    		action='action',
    		title=title,
    		message=message,
    		received_at=datetime.now())

    	if saved:
    		Leed.push_notification()
    		print('leed was saved!')
    '''

    def __repr__(self):
        return '<Leed %s>' % self.id
