# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base

class Page(Base):
    name = db.Column(db.String(50), unique=True)
    link = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(500))
    template = db.Column(db.Integer, db.ForeignKey('template.id'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategory = db.Column(db.Integer, db.ForeignKey('subcategory.id'))

    def __repr__(self):
        return '<Page %s>' % self.name
