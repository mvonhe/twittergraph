from flask import Flask, render_template, request
import os
import twitter_test

app = Flask(__name__)
api = twitter_test.api
print api

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/', methods=['GET'])
def display_template():
	if len(request.args) > 0:

		sname = request.args["screenname"]
		dname = api.GetUser(screen_name=sname).AsDict()['name']
		twitter_test.writeJson(sname)

		#print dname
		return render_template('index.html', screenname=sname, displayName=dname)
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
