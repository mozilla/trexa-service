import os

"""Flask application config module."""

# by default, these are relative to the root directory
ZIP_DOWNLOADS_DEST = 'downloads/zip' or os.environ.get('ZIP_DOWNLOADS_DEST')
CSV_DOWNLOADS_DEST = 'downloads/csv' or os.environ.get('CSV_DOWNLOADS_DEST')
FINAL_LIST_DEST = 'trexa/static/lists' or os.environ.get('FINAL_LIST_DEST')
