# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from ..models import Page, Template
from wtforms_alchemy import ModelForm
from wtforms import TextAreaField, SubmitField, StringField
from flaskckeditor import CKEditor


class AddPageForm(ModelForm, Form):
	
	class Meta:
		model = Page

class AddTemplateForm(ModelForm, Form):
	
	class Meta:
		model = Template