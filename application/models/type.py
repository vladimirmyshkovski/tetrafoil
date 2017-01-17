# coding: utf-8
from ._base import db
from .base import *

class Type(Base):
	
	name = db.Column(db.String(50), unique=True)
	organisations =  db.relationship('Organisation', backref='type_organisations')

