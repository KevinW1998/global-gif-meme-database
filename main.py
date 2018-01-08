from bottle import route, run, template, static_file


@route('/')
def root():
    return template('index.tpl')

@route('/upload_gif')
def upload_gif():
    return template('upload_gif')

@route('/view_gif')
def view_gif():
    return template('view_gif')

@route('/remove_gif')
def remove_gif():
    return template('remove_gif')


if __name__ == '__main__':
    run(host='localhost', port=8080)
