# coding: utf-8
from flask import Blueprint, render_template, jsonify, abort
from flask_restful import Resource, Api
from ..models import User, Product

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)


class USER(Resource):
    def get(self, id):
    	try:
    		user = User.query.get_or_404(id)
    		return jsonify({
    			'User email: ': user.email
    			})
    	except:
    		return 'User {} not found!!!'.format(id)

class PRODUCT(Resource):
    def get(self, id):
    	try:
    		product = Product.query.get_or_404(id)
    		return jsonify({
    			'Product name: ': product.name
    			})
    	except:
    		return 'Product {} not found!!!'.format(id)

api.add_resource(USER, '/user/<int:id>')
api.add_resource(PRODUCT, '/product/<int:id>')