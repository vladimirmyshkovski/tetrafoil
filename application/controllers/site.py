# coding: utf-8
from flask import render_template, Blueprint, request,abort, session, redirect, url_for
from ..forms import AddLeedForm
from ..models import Leed, User, Product, Image, Calculator, Tag


bp = Blueprint('site', __name__)


@bp.route('/create', methods=['POST', 'GET'])
def create():
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
    return render_template('site/products/products.html')


@bp.route('/Продукция/<keyword>')
def product(keyword):
    """Product page."""
    product = Product.query.filter(Product.name == keyword).first()
    product_images = Image.query.filter(Image.product == product.id).all()
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