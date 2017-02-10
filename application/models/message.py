# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

class Message(Base):
	subject = db.Column(db.String(256), nullable=False)
	content = db.Column(db.Text)
	to = db.Column(db.Integer, nullable=False, index=True)
	unread = db.Column(db.Boolean, default=True)
	sent_at = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return 'To: id<{}> \n Sub: {}'.format(self.to, self.subject)

	def dict(self):
		return dict(id=self.id, subject=self.subject, content=self.content, to=self.to, unread=self.unread, sent_at=self.sent_at.isoformat())

