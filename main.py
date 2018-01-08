from bottle import route, run, template, static_file, Bottle

from memedatabase import MemeDatabase

if __name__ == '__main__':
    app = application = Bottle()
    db = MemeDatabase()

    @app.route('/static/images/<picture>')
    def serve_pictures(picture):
        return static_file(picture, root='views/static/images')

    @app.route('/static/css/<css>')
    def css_pictures(css):
        return static_file(css, root='views/static/css')

    @app.route('/')
    def root():
        return template('index.tpl')


    @app.route('/upload_gif')
    def upload_gif():
        return template('upload_gif')


    @app.route('/view_gif')
    def view_gif():
        return template('view_gif')


    @app.route('/remove_gif')
    def remove_gif():
        return template('remove_gif')

    @app.error(404)
    def error404(error):
        return template('404')

    app.run(host='localhost', port=8080)
