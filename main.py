from bottle import route, run, template, static_file


@route('/')
def root():
    return static_file('view/index.tpl', '.')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
