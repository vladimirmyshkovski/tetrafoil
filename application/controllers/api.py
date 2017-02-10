# coding: utf-8
from flask import Blueprint, render_template, jsonify, abort
from flask_restful import Resource, Api
from ..models.user import User

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)


class USER(Resource):
    def get(self, id):
    	try:
    		user = User.query.get_or_404(id)
    		return jsonify({
    			'User email: ': user.email,
    			})
    	except:
    		return 404

    	

api.add_resource(USER, '/user/<int:id>')