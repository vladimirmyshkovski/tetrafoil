# coding: utf-8
from ._base import db
from .base import *

class Role(Base):
	
	name = db.Column(db.String(50), unique=True)
	users =  db.relationship('User', backref='user_role', lazy='dynamic')


