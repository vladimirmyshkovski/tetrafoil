# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

class Calculator(Base):
    inout = db.Column(db.Boolean())
    width_min = db.Column(db.String(50))
    width_max = db.Column(db.String(50))
    width_step = db.Column(db.String(50))
    width_start = db.Column(db.String(50))
    height_min = db.Column(db.String(50))
    height_max = db.Column(db.String(50))
    height_step = db.Column(db.String(50))
    height_start = db.Column(db.String(50))
    product = db.Column(db.Integer, db.ForeignKey('product.id'))


    def __repr__(self):
        return '<Calculator %s>' % self.name
