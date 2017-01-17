# coding: utf-8
from flask import Blueprint, render_template
from ..models import Role, db


bp = Blueprint('admin', __name__)

@bp.route('/admin')
def admin():
	db.create_all()
	role = Role(name='admin')
	db.session.add(role)
	db.session.commit()

