# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm
from ..models import Leed
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class AddLeedForm(ModelForm,Form):
	class Meta:
		model = Leed
