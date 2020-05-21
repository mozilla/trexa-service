import os

from flask import abort
from flask import Blueprint
from flask import current_app
from flask import request
from flask import Response

from trexa.api.helpers import trim_csv

"""Blueprint for API methods."""

api_bp = Blueprint('api_bp', __name__, url_prefix='/api',
                   template_folder='../templates')


@api_bp.route('/')
def index():
    """Nothing to see here."""
    return abort(403)


@api_bp.route('/lists/<path:filename>')
def trim_file(filename):
    """API route to serve count-limited lists.

    If there's no count arg (or its garbage), just serve the whole thing
    by sending None to trim_csv.
    """
    count = request.args.get('count')
    if count.isdigit():
        count = int(count)
    else:
        count = None
    csv_path = os.path.join(current_app.root_path, 'static/lists', filename)
    if not os.path.exists(csv_path):
        return abort(404)
    return Response(trim_csv(csv_path, count=count), mimetype='text/csv')
