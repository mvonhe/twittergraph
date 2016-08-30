from flask import Flask, render_template, request
import os, time, twitter_test, re
from nocache import nocache

app = Flask(__name__)
api = twitter_test.api
#print api

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/', methods=['GET'])
#@nocache
def display_template():
	if len(request.args) > 0:

		sname = request.args["screenname"]
		if re.findall('twitter.com', sname):
			sname = re.sub('.*twitter.com/','',sname)
		dname = api.GetUser(screen_name=sname).AsDict()['name']
		filename = twitter_test.writeJson(sname)
		nfriends=api.GetUser(screen_name=sname).friends_count
		#time.sleep(3)

		print filename
		return render_template('index2.html', screenname=sname, displayName=dname, fname=filename, nfriends=nfriends)
	else:
		return render_template('index2.html')

@app.route('/<uname>', methods=['GET'])
def livesearch(uname):
	if len(uname)>0:
		result=api.GetUsersSearch(uname)
		#print result[1]
		hint=''
		for i in range(5):
			if hint=='':
				hint=result[i].screen_name
			else:
				hint+='<br>'+result[i].screen_name

		print hint

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
