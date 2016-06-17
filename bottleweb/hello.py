from bottle import route,run

@route('/')
def index():
	return "Hello Word!"
run(host="www.test001.com",port=8080)
