from flask import Flask, request, jsonify
import string

app = Flask(__name__)
all_alpha = set(string.ascii_lowercase)
alph_len = len(all_alpha)

@app.route("/")
def main():
	return "init"	


@app.route("/v1/contains-all-alphas/subset", methods=['GET'])
def check():
	str_set = {c.lower() for c in request.args['string']}
	return jsonify({'contains-all-alphas': all_alpha <= str_set})

@app.route("/v1/contains-all-alphas/loop", methods=['GET'])
def checkLoop():
	to_return = {'contains-all-alphas': False}

	if (len(request.args['string']) < alph_len):
		return to_return

	str_set = {c.lower() for c in request.args['string']}
	to_return['contains-all-alphas'] = len([a for a in all_alpha if a in str_set]) == alph_len
	return jsonify(to_return)

if __name__ == '__main__':
	app.run()