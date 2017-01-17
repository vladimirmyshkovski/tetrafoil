# coding: utf-8
from datetime import datetime
from .base import *


class Notification(Base):
	
	created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	has_read = db.Column(db.Boolean)
	action = db.Column(db.String(50))
	title = db.Column(db.String(50))
	message = db.Column(db.String(50))
	received_at = datetime.now()


	def __repr__(self):
		return '<Notification %s>' % self.id
