# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Tag(Base):
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(2500))
    images = db.relationship('Image', backref='image_tags')
    product = db.Column(db.Integer, db.ForeignKey('product.id'))


    def __repr__(self):
        return '%s' % self.name
