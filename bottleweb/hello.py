from bottle import route,run

@route('/')
def index():
    return "hello word"

run(host="localhost",port=9001)
