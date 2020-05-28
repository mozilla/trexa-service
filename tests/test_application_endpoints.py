import pytest

import trexa

"""Tests for the Flask application (non-API) endpoints.

Note: test_list_download relies on these tests being
invoked like so: `FLASK_ENV=development pytest`
"""


@pytest.fixture
def client():
    trexa.app.config.update(
        FINAL_LIST_DEST='tests/fixtures',
        TESTING=True,
    )
    with trexa.app.test_client() as client:
        yield client


def test_useless_homepage(client):
    """Test the index route serves the README.md"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Trexa Service' in rv.data


def test_lists_endpoint(client):
    """Test the lists template is served for /lists

    We point the FINAL_LIST_DEST to the fixtures file for testing."""
    rv = client.get('/lists')
    assert rv.status_code == 200
    assert b'Downloads' in rv.data
    assert b'<a download href="lists/trexa-05-28-2020.csv' in rv.data


if trexa.app.config['ENV'] == 'development':
    def test_list_download(client):
        """This should only pass for local development or tests."""
        print(client.config)
        rv = client.get('/lists/test_file_with_thirty_lines.csv')
        assert rv.status_code == 200
        assert 'text/csv' in rv.headers.get('content-type')
        assert 'attachment' in rv.headers.get('content-disposition')
        assert 'test_file_with_thirty_lines.csv' in rv.headers.get(
            'content-disposition')
        rv = client.get('/lists/garbage.pdf')
        assert rv.status_code == 404
