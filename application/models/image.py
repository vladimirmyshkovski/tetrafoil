# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Image(Base):
    name = db.Column(db.String(50))
    path = db.Column(db.Unicode(128))
    tags = db.relationship(
    	"Tag",
    	secondary='tags_images',
    	back_populates="images")
    product = db.Column(db.Integer(), db.ForeignKey('product.id'))
    category = db.Column(db.Integer(), db.ForeignKey('category.id'))

    def __repr__(self):
        return '%s' % self.name