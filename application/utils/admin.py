from flask_admin import Admin, expose, form
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form.upload import ImageUploadField
import os
import os.path as op
from flask_admin.contrib.sqla import ModelView
from ..models import User, db, Category, Product, Image, Tag, Size, Calculator, City, Country
from flask_admin.form import BaseForm
from sqlalchemy.event import listens_for
from flask_admin.contrib import sqla
from jinja2 import Markup
from flask import url_for, session, request
from ..utils.babel import babel 
from wtforms import TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_admin.form.fields import Select2Field
from flask.ext.admin.form import Select2Widget

admin = Admin(name='CMS', template_mode='bootstrap3')


static_path = op.join(op.dirname(__file__), '../static')
page_path = op.join(op.dirname(__file__), '../pages')
product_path = op.join(op.dirname(__file__), '../static/img/product_images')
category_path = op.join(op.dirname(__file__), '../static/img/category_images')
file_path = op.join(op.dirname(__file__), '/static/img/product_images')


@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'ru')



class MyAdmin(FileAdmin):
	editable_extensions = ('md', 'html', 'txt', 'js', 'css')



class MyLastAdmin(FileAdmin):
	editable_extensions = ('md', 'html', 'txt', 'js', 'css')



class ProductView(ModelView):

  column_hide_backrefs = False
  form_overrides = {
  'description': TextAreaField,
  'property': TextAreaField,
  'article': TextAreaField
  }
  '''
  form_extra_fields = {
        'images': QuerySelectField(query_factory=lambda: Image.query.all(), get_label='path')
    }
  '''
  form_extra_fields = {
        'images': sqla.fields.QuerySelectField(
            label='path',
            query_factory=lambda: Image.query.all(),
            widget=Select2Widget(),
            get_label='path'
        )
    }

  form_widget_args = {
    'description': {
        'rows': 5,
        'style': 'font-family: monospace;'
    },
    'property': {
        'rows': 5,
        'style': 'font-family: monospace;'
    },
    'images': {
        'style': 'font-family: monospace;'
    }
  }

  column_display_all_relations = True



  def _list_thumbnail(view, context, model, name):
    if not model.path:
      return ''

    return Markup('<img src="%s" style="width: 250px; height: 250px">' % url_for('static',
      filename=form.thumbgen_filename(model.path)))

  inline_models = [(Image,
    dict(
      form_excluded_columns = ['created_at', 'modified_at'],
      column_formatters = {'path': _list_thumbnail},
      form_extra_fields = {
      'path': form.ImageUploadField('Картинка',
        base_path=product_path,
        thumbnail_size=(50, 50, True),
        url_relative_path='/img/product_images')
      })), 
  (Calculator, 
    dict(
      form_excluded_columns = ['created_at', 'modified_at']
      ))
  ]

  column_formatters = {
  'path': _list_thumbnail
  }

  form_excluded_columns = ['created_at', 'modified_at', 'size']
  column_exclude_list = ('created_at', 'modified_at', 'size')



class CategoryView(ModelView):
  form_excluded_columns = ['created_at', 'modified_at']

  column_display_all_relations = True

  def _list_thumbnail(view, context, model, name):
    if not model.path:
      return ''


    return Markup('<img src="%s">' % url_for('static',
      filename=form.thumbgen_filename(model.path)))

  inline_models = [(Image,
    dict(
      form_excluded_columns = ['created_at', 'modified_at'],
      column_formatters = {'path': _list_thumbnail},
      form_extra_fields = {
      'path': form.ImageUploadField('Path',
        base_path=product_path,
        thumbnail_size=(250, 250, True),
        url_relative_path='static/img/product_images')
      }
      )
    )
  ]

  column_formatters = {
  'path': _list_thumbnail
  }

  form_excluded_columns = ['created_at', 'modified_at']
  column_exclude_list = ('created_at', 'modified_at')



class ImageView(ModelView):
  form_overrides = {
  'path': form.FileUploadField
  }

  form_args = {
  'path': {
  'label': 'Картинка',
  'base_path': 'img/product_images/',
  'allow_overwrite': True
  },
  'name': {
  'label': 'Название'
  },
  'tags': {
  'label': 'Тэги'
  }
  }
  def _list_thumbnail(view, context, model, name):
    if not model.path:
      return ''

      return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.path)))

    column_formatters = {
    'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=product_path,
                                      thumbnail_size=(250, 250, True))
    }



admin.add_view(ProductView(Product, db.session))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ModelView(Size, db.session))
admin.add_view(ModelView(Tag, db.session))
#admin.add_view(ModelView(Image, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(MyAdmin(static_path, '/static/', name='Static Files'))
admin.add_view(MyLastAdmin(page_path, '/pages/', name='Pages'))
admin.add_view(ModelView(Country, db.session))
admin.add_view(ModelView(City, db.session))
