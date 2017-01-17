# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Country(Base):
    name = db.Column(db.String(50), unique=True)
    coordinates = db.Column(db.String(255), unique=True)
    organisations = db.relationship('Organisation', backref='country_organisations')
    cities = db.relationship('City', backref='country_sities')


    def __repr__(self):
        return '<Country %s>' % self.name
