from flask.testing import FlaskClient


def test_game(client: FlaskClient):
    resp = client.get('/game')
    assert resp.status_code == 200


def test_index(client: FlaskClient):
    resp = client.get('/')
    assert resp.status_code == 302
    assert 'game' in resp.headers['Location']


def test_no_url_found(client: FlaskClient):
    resp = client.get('/a-random-url')
    assert resp.status_code == 404
    assert b'Page not found' in resp.data
