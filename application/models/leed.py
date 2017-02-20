# coding: utf-8
from datetime import datetime
from .base import *
from ..models import Notification

class Leed(Base):
    
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Leed %s>' % self.id
