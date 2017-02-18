# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

tags_images = db.Table('tags_images', Base.metadata,
    db.Column('tags_ids', db.Integer, db.ForeignKey('tag.id')),
    db.Column('images_ids', db.Integer, db.ForeignKey('image.id'))
)

class Tag(Base):
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(2500))
    images = db.relationship(
    	"Image",
    	secondary=tags_images,
    	back_populates="tags")
    product = db.Column(db.Integer, db.ForeignKey('product.id'))


    def __repr__(self):
        return '%s' % self.name
