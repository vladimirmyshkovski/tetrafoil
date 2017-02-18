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
    image = db.relationship('Image', backref='Картинки продукта')
    tags = db.relationship('Tag', backref='Тэги проудкта')
    calculator = db.relationship('Calculator', backref="Калькуляторы продукта")


    def __repr__(self):
        return '%s' % self.name