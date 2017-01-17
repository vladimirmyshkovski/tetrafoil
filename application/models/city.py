# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class City(Base):
    name = db.Column(db.String(50), unique=True)
    country = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False, info={"label": "Country"})
    coordinates = db.Column(db.String(255), unique=True)
    organisations = db.relationship('Organisation', backref='city_organisations')


    def __repr__(self):
        return '<City %s>' % self.name
