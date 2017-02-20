# coding: utf-8
from ._base import db
from .base import *

class Status(Base):
	
	name = db.Column(db.String(50), unique=True)
	projects =  db.relationship('Project', backref='status_projects')


