# coding: utf-8
from flask import Blueprint, render_template
from ..models import Role, db
from ..utils.permissions import AdminPermission


bp = Blueprint('admin', __name__)

@bp.route('/admin')
@AdminPermission()
def admin():
	return render_template('site/index/index.html')

