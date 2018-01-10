import os

from bottle import route, run, template, static_file, Bottle, abort, request

from memedatabase import MemeDatabase

if __name__ == '__main__':
    # Settings
    path_for_dynamic_storage = "views/dynamic/images/"
    path_for_display = "/dynamic/images/"

    app = application = Bottle()
    db = MemeDatabase()
    print("Startup... all files:")
    print(list(map(lambda file_ref: (file_ref[0], path_for_display + file_ref[1]), db.get_all_file_references())))

    @app.route('/static/images/<picture>')
    def serve_pictures(picture):
        return static_file(picture, root='views/static/images')

    @app.route('/static/css/<css>')
    def css_pictures(css):
        return static_file(css, root='views/static/css')

    @app.route('/dynamic/images/<image>')
    def serve_dyn_image(image):
        return static_file(image, root='views/dynamic/images')

    @app.route('/')
    def root():
        # Get all path references and add path prefix
        memes = list(map(lambda file_ref: (str(file_ref[0]), path_for_display + file_ref[1]), db.get_all_file_references()))
        print("Showing memes")
        print(memes)
        return template('index.tpl', memes=memes)

    @app.route('/upload_gif', method='POST')
    def upload_gif():
        upload = request.files.get('upload')
        if upload is None:
            return "No file selected"

        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.gif', '.jpg', '.jpeg', '.png', '.bmp'):
            return "File extension not allowed."

        save_path = path_for_dynamic_storage
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        new_id = db.get_next_free_id()  # Next free id
        new_filename = db.create_safe_filename(upload.filename)  # Create safe filename --> in case two images has the same filename
        file_to_save = save_path + new_filename  # prefix it with the path
        upload.save(file_to_save)  # Save the file
        db.save_file_reference(new_filename)  # Save the reference in the database

        # return template('upload_gif')
        return template('view_gif', id=new_id, meme=path_for_display + new_filename, new_file=False)

    # TODO: How to handle relative?
    @app.route('/view_gif/<id>')
    def view_gif(id):
        file_ref = db.get_file_reference_or_none(id)
        if file_ref is None:
            abort(404)
        return template('view_gif', id=file_ref[0], meme=path_for_display + file_ref[1], new_file=False)


    # TODO: How to handle relative?
    @app.route('/remove_gif/<id>')
    def remove_gif(id):
        success = db.remove_file_reference(id)
        if not success:
            abort(404)
        return template('remove_gif')

    @app.error(404)
    def error404(error):
        return template('404')

    app.run(host='localhost', port=8080)
