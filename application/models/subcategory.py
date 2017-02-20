# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Subcategory(Base):
    name = db.Column(db.String(50), unique=True)
    link = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Subcategory %s>' % self.name
