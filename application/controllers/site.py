# coding: utf-8
from flask import render_template, Blueprint, request,abort
from ..forms import AddLeedForm
from ..models import Leed, User

bp = Blueprint('site', __name__)

@bp.route('/create', methods=['POST'])
def create():
    leed = Leed()
    form = AddLeedForm()
    if form.validate_on_submit():
        leed.create(**form.data)
        user = User.query.get(1)
        User.create_notification(
            self=user,
            action='action',
            title='New leed was created!',
            message='Hurry, or you will be late!')
    return 'form is submited!'


@bp.route('/Главная')
@bp.route('/')
def index():
    """Index page."""
    return render_template('site/index/index.html')


@bp.route('/Производственные возможности')
def manufactory():
    """Manufactory page."""
    return render_template('site/page/page.html', 
    	keyword 	= 'Производственные возможности',
    	image		= 'block_1',
    	text		= 'Будучи непосредственно производителем термотрансферной ленты, мы имеем в своем распоряжении высокотехнологичную производственную линию и все подразделения, необходимые для полноценного обслуживания клиентов.'
    	)


@bp.route('/Индивидуальное изготовление')
def individual():
    """Individual page."""
    return render_template('site/page/page.html', 
    	keyword 	= 'Индивидуальное изготовление',
    	image		= 'block_2',
    	text		= 'Испытываете потребность в размере и материале риббона, отличном от уже имеющихся в ассортименте? Мы готовы выполнить приватный заказ на термотрансферную и текстильную ленту и прочие расходные материалы. Наши специалисты окажут помощь в выборе и решении сложных и нестандартных задач по маркировке.'
    	)


@bp.route('/Склад')
def stock():
    """Individual page."""
    return render_template('site/page/page.html', 
    	keyword 	= 'Склад',
    	image		= 'block_3',
    	text		= 'Ска-ска-ска'
    	)


@bp.route('/Бесплатные образцы')
def free():
    """Individual page."""
    return render_template('site/page/page.html', 
        keyword     = 'Склад',
        image       = 'block_3',
        text        = 'Предлагаемые нами термотрансферные ленты обладают отличной износостойкостью и высоким качеством печати, соответствующим требованиям производителей печатной техники. Чтобы вы могли удостовериться в этом лично и убедить своих клиентов, мы предлагаем образцы выпускаемых риббонов на совершенно безвозмездной основе.'
        )


@bp.route('/Технические характеристики')
def technical():
    """Individual page."""
    return render_template('site/page/page.html', 
    	keyword 	= 'Технические характеристики',
    	image		= 'block_4',
    	text		= 'Термотрансферная лента имеет довольно сложное строение, основой которого является полиэстерная пленка. С одной стороны, ее покрывают цветным красящим веществом, с другой – специфической смазкой. Задача последней – предотвращать трение между лентой и термоголовкой устройства. Мы предлагаем красящие ленты с различным типом основы.'
    	)


@bp.route('/Доставка и оплата услуг')
def delivery():
    """Individual page."""
    return render_template('site/page/page.html', 
        keyword     = 'Склад',
        image       = 'block_3',
        text        = 'Оплата товара, сроки его изготовления и последующая доставка прописываются в двустороннем договоре о сотрудничестве.'
        )

@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about/about.html')

@bp.route('/products')
def products():
    """Products page"""
    return render_template('site/products/products.html')

@bp.context_processor
def form():
    LeedForm = AddLeedForm(request.form)
    return dict(form=LeedForm)
