# coding: utf-8
from ._base import db
from .base import *
from flask_security import RoleMixin


class Role(Base, RoleMixin):
	
	name = db.Column(db.String(50), unique=True)
	description = db.Column(db.String(255))


