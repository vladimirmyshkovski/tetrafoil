# coding: utf-8
from flask import render_template, Blueprint, request,abort, session, redirect, url_for
from ..forms import AddLeedForm
from ..models import Leed, User, Product, Image, Calculator, Tag, Category
#from sqlalchemy import desc
from collections import OrderedDict
bp = Blueprint('site', __name__)


from flask_mail import Message
from ..utils.mail import mail

@bp.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        params = request.form
        email = params['email']
        phone = params['phone']
        msg = Message("Заявка" + str(request.url_root),
        sender="SiegHeil@1488.hh",
        recipients=["narnikgamarnikus@gmail.com"])
        msg.body = "Заявка со страницы " + str(request.base_url) + "/n" + "E-mail " + str(email) + "/n" + "Phone " + str(phone) + "/n" + "ID" + str(id)
        msg.html = "<h1>Заявка со страницы "  + str(request.base_url)  +  "</h1>" + "<p>E-mail " + str(email) + "</p>" +  "<p>Phone "  + str(phone) + "</p>" + "<p>ID " + str(id) + "</p>"
        
        mail.send(msg)
        leed = Leed()
        form = AddLeedForm()
        if form.validate_on_submit():
            leed.create(**form.data)
            user = User.query.get(1)
            session['leed_name'] = form.email.data
            print(session['leed_name'])
            User.create_notification(
                self=user,
                action='action',
                title='New leed was created!',
                message='Hurry, or you will be late!')
    return redirect(url_for('site.index'))


@bp.route('/Главная', methods=['GET'])
@bp.route('/', methods=['GET'])
def index():
    """Index page."""
    return render_template('site/index/index.html')


@bp.route('/О компании')
def about():
    """About page."""
    return render_template('site/about/about.html')


@bp.route('/Продукция')
def products():
    """Products page."""

    asd = {c.name : {p.name : p.image for p in Product.query.filter(Product.category == c.id).order_by(Product.position.desc()) } for c in Category.query.order_by(Category.position.desc())} 
    print(OrderedDict(sorted(asd.items()), key=lambda t: len(t[0])))
    return render_template('site/products/products.html', asd=asd, Product=Product, Category=Category)


@bp.route('/Продукция/<keyword>')
def product(keyword):
    """Product page."""
    product = Product.query.filter(Product.name == keyword).first()
    print(product)
    product_images = Image.query.filter(Image.product == product.id).all()
    print(product_images)
    calculator = Calculator.query.filter(Calculator.product == product.id).first()
    return render_template('site/product/product.html',
        product=product,
        product_images=product_images,
        calculator=calculator)


@bp.route('/Технические характеристики')
def technical():
    """Technicals page."""
    return render_template('site/technical/technical.html')


@bp.route('/Образцы')
def sample():
    """Sample page."""
    return render_template('site/sample/sample.html')


@bp.route('/Доставка')
def divelery():
    """Divelery page."""
    return render_template('site/divelery/divelery.html')