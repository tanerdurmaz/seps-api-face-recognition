import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>seps api for face recognition, version 1.</p>"

@app.route('/api/face/<url>', methods=['GET'])
def api_all(url):
	return "kek"
app.run()