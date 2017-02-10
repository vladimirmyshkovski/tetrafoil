# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Product(Base):
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(2500))
    property = db.Column(db.String(2500))
    article = db.Column(db.String(2500))
    price = db.Column(db.String(10))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    image = db.relationship('Image', backref='product_images')
    tags = db.relationship('Tag', backref='products_tags')
    size = db.relationship('Size', backref='products_sizes')
    calculator = db.relationship('Calculator', backref='products_calculator')


    def __repr__(self):
        return '%s' % self.name