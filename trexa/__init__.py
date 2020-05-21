import os

from flask import abort
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import url_for
import markdown

from trexa.api.endpoints import api_bp

app = Flask(__name__)
app.config.from_object('trexa.config')

for blueprint in [api_bp]:
    app.register_blueprint(blueprint)


@app.route('/')
def index():
    """Create the index route.

    This module isn't intended to serve a useful website, so we just dump
    the README.md as HTML.
    """
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read()
    )
    return md_template_string


@app.route('/lists')
def show_downloads():
    """Route to show all downloads."""
    files = os.listdir(app.config['FINAL_LIST_DEST'])
    return render_template('list.html', files=files)


if app.config['ENV'] == 'development':
    @app.route('/lists/<file_name>')
    def serve_downloads(file_name):
        """Dev-only route to serve downloads.

        NGINX will handle static assets on the production server."""
        lists_path = os.path.join(app.root_path, 'static/lists')
        if not os.path.exists(f'{lists_path}/{file_name}'):
            return abort(404)
        return send_from_directory('static/lists', file_name,
                                   as_attachment=True, mimetype='text/csv')
