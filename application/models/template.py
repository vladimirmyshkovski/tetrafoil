# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Template(Base):
    name = db.Column(db.String(50), unique=True)
    html = db.Column(db.String(5000), unique=True)

    def __repr__(self):
        return '<Template %s>' % self.name
