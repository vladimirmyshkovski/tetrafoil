# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm
from ..models import Organisation, Contact, User, Project, Activity, Invoice, City, Country, Type
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def available_cities():
	return City.query.all()

def available_countries():
	return Country.query.all()

def available_organisations():
	return Organisation.query.all()

def available_types():
	return Type.query.all()

def available_contacts():
	return Contact.query.all()

def available_projects():
	return Project.query.all()

def available_invoices():
	return Invoice.query.all()

def available_activities():
	return Activity.query.all()



class AddOrganisationForm(ModelForm, Form):
	"""Add organisation form"""

	class Meta:
		model = Organisation

	country = QuerySelectField('Country', query_factory=available_countries, get_label='name')
	city = QuerySelectField('City', query_factory=available_cities, get_label='name')
	type = QuerySelectField('Type', query_factory=available_types, get_label='name')
	contacts = QuerySelectField('Contact', query_factory=available_contacts, get_label='name')
	activities = QuerySelectField('Activity', query_factory=available_activities, get_label='name')


class AddContactForm(ModelForm, Form):
	"""Add contact form"""	
	org_id = QuerySelectField('Organisation', query_factory=available_organisations, get_label='name')

	class Meta:
		model = Contact


class AddProjectForm(ModelForm, Form):
	"""Add project form"""
	org_id = QuerySelectField('Organisation', query_factory=available_organisations, get_label='name')
	contact_id = QuerySelectField('Contact', query_factory=available_contacts, get_label='last_name')

	class Meta:
		model = Project


class AddActivityForm(ModelForm, Form):
	"""Add project form"""
	org_id = QuerySelectField('Organisation', query_factory=available_organisations, get_label='name')
	contact_id = QuerySelectField('Contact', query_factory=available_contacts, get_label='last_name')
	project_id = QuerySelectField('Projects', query_factory=available_projects, get_label='end_date')

	class Meta:
		model = Activity


class AddInvoiceForm(ModelForm, Form):
	"""Add invoice form"""
	project_id = QuerySelectField('Projects', query_factory=available_projects, get_label='end_date')

	class Meta:
		model = Invoice