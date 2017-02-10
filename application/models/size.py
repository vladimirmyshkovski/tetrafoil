# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

class Size(Base):
	price = db.Column(db.String(50))
	width = db.Column(db.String(50))
	height = db.Column(db.String(50))
	count = db.Column(db.String(50))
	type = db.Column(db.String(50))
	description = db.Column(db.String(2500))
	product = db.Column(db.Integer, db.ForeignKey('product.id'))


	def __repr__(self):
		return '<Size %s>' % self.name
