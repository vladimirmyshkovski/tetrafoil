# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm, ModelFormField
from ..models import Leed, Country, City, Contact, Product, Address
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class AddLeedForm(ModelForm,Form):
	class Meta:
		model = Leed


class AddCountryForm(ModelForm):
	class Meta:
		model = Country
		only = ['name']

class AddCityForm(ModelForm):
	class Meta:
		model = City
		only = ['name']


class AddAddressForm(ModelForm):
	class Meta:
		model = Address
		only = ['index']


class AddSampleForm(Form):
	name = ModelFormField(AddCountryForm)
	name = ModelFormField(AddCityForm)
	index = ModelFormField(AddAddressForm)