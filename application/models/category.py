# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Category(Base):
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(250))
    products = db.relationship('Product', backref='Category')
    image = db.relationship('Image', backref='Картинка категорий')

    
    def __repr__(self):
        return '%s' % self.name
