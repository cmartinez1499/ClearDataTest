from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flasgger import Swagger

import string

app = Flask(__name__)
api = Api(app)

swagger = Swagger(app)

all_alpha = set(string.ascii_lowercase)
alph_len = len(all_alpha)

parser = reqparse.RequestParser()
parser.add_argument('string', type=str)

resource_fields = {
    'contains-all-alphas':   fields.Boolean
}		

class Assignment1(Resource):
	@marshal_with(resource_fields)
	def get(self):
		"""Checks if string contains ever lever in alphabet
	    This implementation checks if alpha set is a subset of string
	    ---
	    parameters:
	      - name: string
	        in: query
	        type: string
	        required: true
	        schema:
	            type: string
	            minimum: 1
	        default: all
	    responses:
	      200:
	        description: Boolean denoting if string contains all letters of alphabet
	        examples:
	          contains-all-alphas: true
	    """
		args = parser.parse_args(strict=True)
		str_set = {c.lower() for c in args['string']}
		return {'contains-all-alphas': all_alpha <= str_set}

class Assignment2(Resource):
	@marshal_with(resource_fields)
	def get(self):
		"""Checks if string contains ever lever in alphabet
	    This implementation loops through alpha to find each letter in string
	    ---
	    parameters:
	      - name: string
	        in: query
	        type: string
	        required: true
	        schema:
	            type: string
	            minimum: 1
	        default: all
	    responses:
	      200:
	        description: Boolean denoting if string contains all letters of alphabet
	        examples:
	          contains-all-alphas: true
	    """
		to_return = {'contains-all-alphas': False}
		args = parser.parse_args(strict=True)

		if (len(args['string']) < alph_len):
			return to_return

		str_set = {char.lower() for char in args['string']}
		to_return['contains-all-alphas'] = len([letter for letter in all_alpha if letter in str_set]) == alph_len
		return to_return

api.add_resource(Assignment1, '/v1/contains-all-alphas/subset')
api.add_resource(Assignment2, '/v1/contains-all-alphas/loop')

if __name__ == '__main__':
	app.run(debug=True)