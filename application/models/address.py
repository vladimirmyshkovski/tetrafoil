# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

class Address(Base):
    name = db.Column(db.String(50), unique=True)
    index = db.Column(db.String(50))
    #foreign city
    #foreign country
    #foreign org
    #foreign contact
    #foreign user

    def __repr__(self):
        return '%s' % self.name
