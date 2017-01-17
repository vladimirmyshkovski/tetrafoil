# coding: utf-8
from flask import render_template, Blueprint, redirect, request, url_for, g, flash, abort, session
from ..utils.account import signin_user, signout_user
from ..utils.permissions import VisitorPermission, UserPermission
from ..models import db, User, Organisation, Contact, Project, Activity, Invoice, Base, Notification, Leed
from ..forms import AddOrganisationForm, AddContactForm, AddProjectForm, AddActivityForm, AddInvoiceForm, AddLeedForm

bp = Blueprint('crm', __name__)


@bp.route('/post', methods=['GET', 'POST', 'PUT'])
@UserPermission()
def post():
    """POST page"""
    item_id = request.form['pk']
    request_url = request.form['url']
    item_value = request.form['value']
    column_name = request.form['name']
    baselist = [User, Organisation, Contact, Project, Activity, Invoice]
    for i in baselist:
        if str(i.__tablename__) == str(request_url.split('/')[-1][:-1]):
            i = i.query.get(item_id)
            setattr(i, column_name, item_value)
            db.session.add(i)
            db.session.commit()

    return render_template('site/index/index.html')


@bp.route('/crm', methods=['GET', 'POST'])
@UserPermission()
def crm():
    """Index page"""
    return render_template('site/index/index.html')


@bp.route('/add/<keyword>', methods=['GET', 'POST'])
@UserPermission()
def add(keyword):
    """Add """
    baselist = [User, Organisation, Contact, Project, Activity, Invoice, Leed]
    formlist = [AddOrganisationForm, AddContactForm, AddProjectForm, AddActivityForm, AddInvoiceForm, AddLeedForm]
    for i in baselist:
        if str(i.__tablename__) == keyword:
            for f in formlist:
                if (str(str(f.__name__).replace('Add', '')).replace('Form', '')) == str(i.__tablename__).capitalize():
                    form = f()
                    if form.validate():
                        for key, value in form.data.items():
                            cal = getattr(form, key)
                            if key.endswith('_id') is True:
                                print(key)
                                cal.data = cal.data.id
                                setattr(form, key, cal.data)
                        if i.created_by:
                            i.create(**form.data, created_by=g.user.id)
                            print(i)
                            print(i.created_by)
                        else:
                            i.create(**form.data)
                        return redirect(url_for('crm.view', keyword=keyword))
                    return render_template('crm/add/add.html', keyword=keyword, form=form)
    return render_template('crm/add/add.html', keyword=keyword, form=form)


@bp.route('/view/<keyword>', methods=['GET', 'POST'])
@UserPermission()
def view(keyword):
    """View"""
    user_room = 'user_{}'.format(session['user_id'])
    print(user_room)
    print('какого хуя перезагружается роут блеач?')
    user = User.query.get(g.user.id)
    baselist = [User, Organisation, Contact, Project, Activity, Invoice, Notification, Leed]
    for i in baselist:
        if str(i.__tablename__) == keyword:
            table = i.query.filter_by(created_by=g.user.id).all()
            columns = [o.key for o in i.__table__.columns]

    '''
    socketio.emit('message',
        {'data': 'blah '},
        namespace='/notifs',
        room=user_room)'''
    return render_template('crm/view/view.html', columns=columns, table=table, keyword=keyword)

'''
@bp.route('/update/<table>/<id>', methods=['GET', 'POST'])
@UserPermission()
def update(table, id):
    pass
'''