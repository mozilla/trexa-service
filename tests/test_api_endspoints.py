import pytest

import trexa

"""Tests for the API Blueprint module."""


@pytest.fixture
def client():
    trexa.app.config.update(
        FINAL_LIST_DEST='tests/fixtures',
        TESTING=True,
    )
    with trexa.app.test_client() as client:
        yield client


def test_index(client):
    """Test that we do nothing useful for the API index."""
    rv = client.get('/api/')
    assert rv.status_code == 403


def test_api_download(client):
    """Test downloading files from the API endpoint."""
    rv = client.get('/api/lists/05-28-2020')
    assert rv.status_code == 200
    rv = client.get('/api/lists/05-28-2020?count=2')
    assert rv.status_code == 200
    rv = client.get('/api/lists/05-28-2020?lol=wat')
    assert rv.status_code == 200
    rv = client.get('/api/lists/what_in_the_world.py')
    assert rv.status_code == 404


def test_api_download_length(client):
    """Test the count param works as expected."""
    rv = client.get('/api/lists/05-28-2020?count=10')
    # pop off the last empty list item (because '\n' comes at the end)
    assert len(rv.data.split(b'\n')[:-1]) == 10
    assert b'11, login.tmall.com' not in rv.data
    rv = client.get('/api/lists/05-28-2020?a=b&count=10')
    assert len(rv.data.split(b'\n')[:-1]) == 10
    assert b'11, login.tmall.com' not in rv.data
    rv = client.get('/api/lists/05-28-2020?count=')
    assert len(rv.data.split(b'\n')[:-1]) == 30
