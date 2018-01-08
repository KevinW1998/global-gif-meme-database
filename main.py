from bottle import route, run, template, static_file


@route('/')
def root():
    return template('index.tpl')

@route('/upload_gif')
def upload_gif():
    return template('upload_gif')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
    run(host='localhost', port=8080)
