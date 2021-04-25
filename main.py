import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>seps xd.</p>"

@app.route('/api', methods=['GET'])
def api():
	username = request.args.get('username')
	print(username)
	password= request.args.get('password')
	print(password)
	return "<h1>Distant  Archive</h1>" + username + " " + password
