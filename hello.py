from flask import Flask, render_template, request
import os

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/', methods=['GET'])
def display_template():
	'''if len(request.args) > 0:
		print len(request.args)
		_in = request.args["userinput"]
		_sub = request.args["submit"]
		if _sub.lower() == "uppercase":
			_in = _in.upper()
		elif _sub.lower() == "lowercase":
			_in = _in.lower()
		return render_template('index.html', inp = _in)
	'''
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
